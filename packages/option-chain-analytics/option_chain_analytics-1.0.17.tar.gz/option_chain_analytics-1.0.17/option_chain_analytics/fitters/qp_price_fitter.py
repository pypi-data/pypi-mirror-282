"""
fit spline to prices
example usage in volatility_book/ch_implied_vol/fit_price_spline
"""
import pandas as pd
import numpy as np
import cvxpy as cvx
from numba import njit
from typing import Optional, Tuple
from enum import Enum

from option_chain_analytics.fitters.utils import imply_bid_ask_mark_vols, SliceFitOutputs
from option_chain_analytics.option_chain import SliceColumn
from scipy.interpolate import make_interp_spline, BSpline

from option_chain_analytics.utils.implied_forwards import imply_forward_discount_from_bid_ask_prices
from option_chain_analytics.utils.numerics import set_matrix_d1_d2


class WeightType(Enum):
    IDENTITY = 1
    TIME_VALUE = 2
    BID_ASK_SPREAD = 3
    ABS_MONEYNESS = 4


def fit_slice_mark_prices_implied_vols_with_qp_solver(slice_df: pd.DataFrame,
                                                      weight_type: WeightType = WeightType.TIME_VALUE,
                                                      eps: float = 0.0001,
                                                      bid_ask_contraint_band: float = 0.99,  # will also be multpilied by weights
                                                      verbose: bool = False
                                                      ):
    """
    slice_df must be indexed by strikes
    fit mark prices and compute implied vols
    """
    calls = slice_df.loc[slice_df[SliceColumn.OPTION_TYPE.value] == 'C', :]
    puts = slice_df.loc[slice_df[SliceColumn.OPTION_TYPE.value] == 'P', :]
    out = imply_forward_discount_from_bid_ask_prices(calls_bid_ask=calls[[SliceColumn.BID_PRICE, SliceColumn.ASK_PRICE]],
                                                     put_bid_ask=puts[[SliceColumn.BID_PRICE, SliceColumn.ASK_PRICE]])

    if out is not None:
        forward, discfactor = out
        print(f"implied forward={forward}, discfactor2={discfactor}")
    else:
        forward = float(np.nanmean(slice_df[SliceColumn.SPOT_PRICE.value]))
        discfactor = 1.0
        print(f"failed to imply forward: using spot proce = {forward} and discfactor={discfactor}")

    mark_prices = infer_call_put_prices_with_qp_solver(slice_df=slice_df,
                                                       forward=forward,
                                                       discfactor=discfactor,
                                                       weight_type=weight_type,
                                                       eps=eps,
                                                       is_reindex_to_slice_strikes=True,
                                                       bid_ask_contraint_band=bid_ask_contraint_band,
                                                       verbose=verbose)

    call_mark_prices = mark_prices.iloc[:, 0]
    put_mark_prices = mark_prices.iloc[:, 1]

    ttm = slice_df[SliceColumn.TTM].iloc[0]
    calls_bid = calls[SliceColumn.BID_PRICE].to_numpy(float)  # do not change the raw data
    calls_ask = calls[SliceColumn.ASK_PRICE].to_numpy(float)
    puts_bid = puts[SliceColumn.BID_PRICE].to_numpy(float)
    puts_ask = puts[SliceColumn.ASK_PRICE].to_numpy(float)
    call_strikes = calls[SliceColumn.STRIKE].to_numpy(float)
    put_strikes = puts[SliceColumn.STRIKE].to_numpy(float)

    calls_bid_iv, calls_ask_iv, calls_mark_iv = imply_bid_ask_mark_vols(strikes=call_strikes,
                                                                        bid_prices=calls_bid,
                                                                        ask_prices=calls_ask,
                                                                        mark_prices=call_mark_prices.to_numpy(),
                                                                        ttm=ttm,
                                                                        forward=forward,
                                                                        discfactor=discfactor,
                                                                        optiontype='C')

    puts_bid_iv, puts_ask_iv, puts_mark_iv = imply_bid_ask_mark_vols(strikes=put_strikes,
                                                                     bid_prices=puts_bid,
                                                                     ask_prices=puts_ask,
                                                                     mark_prices=put_mark_prices.to_numpy(),
                                                                     ttm=ttm,
                                                                     forward=forward,
                                                                     discfactor=discfactor,
                                                                     optiontype='P')
    slice_fit_outputs = SliceFitOutputs(forward=forward,
                                        discfactor=discfactor,
                                        call_mark_prices=call_mark_prices,
                                        put_mark_prices=put_mark_prices,
                                        calls_bid_iv=calls_bid_iv,
                                        calls_ask_iv=calls_ask_iv,
                                        calls_mark_iv=calls_mark_iv,
                                        puts_bid_iv=puts_bid_iv,
                                        puts_ask_iv=puts_ask_iv,
                                        puts_mark_iv=puts_mark_iv)
    return slice_fit_outputs


def infer_call_put_prices_with_qp_solver(slice_df: pd.DataFrame,
                                         forward: float,
                                         discfactor: float,
                                         weight_type: WeightType = WeightType.TIME_VALUE,
                                         eps: float = 0.0001,
                                         bid_ask_contraint_band: float = 0.99,  # deflate / inflate
                                         call_slice_name: str = 'call',
                                         put_slice_name: str = 'put',
                                         verbose: bool = True,
                                         is_reindex_to_slice_strikes: bool = False,
                                         total_num_of_iterations: int = 5
                                         ) -> pd.DataFrame:
    """
    given slices infer call and put marks
    """
    calls_slice = slice_df.loc[slice_df[SliceColumn.OPTION_TYPE.value] == 'C', :]
    puts_slice = slice_df.loc[slice_df[SliceColumn.OPTION_TYPE.value] == 'P', :]

    for n in np.arange(total_num_of_iterations):
        call_marks, put_marks = infer_mark_call_put_price_with_qp_solver(
            call_bid_ask_prices=calls_slice[[SliceColumn.BID_PRICE, SliceColumn.ASK_PRICE]],
            put_bid_ask_prices=puts_slice[[SliceColumn.BID_PRICE, SliceColumn.ASK_PRICE]],
            forward_price=forward,
            discfactor=discfactor,
            eps=eps,
            bid_ask_contraint_band=bid_ask_contraint_band,
            weight_type=weight_type,
            verbose=verbose)
        if call_marks is not None:
            print(f"solved iteration={n+1} with eps={eps}, bid_ask_contraint_band={bid_ask_contraint_band}")
            break
        else:
            print(f"unsolved iteration={n+1} with eps={eps}, bid_ask_contraint_band={bid_ask_contraint_band}"
                  f" reducing eps by 0.1 and increasing bid_ask_contraint_band by 5.0 ")
            eps *= 0.1
            bid_ask_contraint_band *=2.0

    mark_prices = pd.concat([call_marks, put_marks], axis=1).sort_index()
    if is_reindex_to_slice_strikes:  # reindex to given strikes
        slice_strikes = pd.Index(slice_df[SliceColumn.STRIKE.value].unique())
        mark_prices = mark_prices.reindex(index=slice_strikes).sort_index()

    return mark_prices


def compute_eror_weights(weight_type: WeightType,
                         strikes: np.ndarray,
                         bid_price: np.ndarray,
                         ask_price: np.ndarray,
                         forward_price: float,
                         is_calls: bool
                         ) -> np.ndarray:
    """
    set error weights for QP problem
    """
    # set error weights
    if weight_type == WeightType.IDENTITY:
        w = np.identity(strikes.shape[0])

    elif weight_type == WeightType.TIME_VALUE:
        mid_price = 0.5 * (bid_price + ask_price)
        # floor time_value to 1e-8
        if is_calls:
            time_value = np.maximum(mid_price - np.maximum(forward_price - strikes, 0.0), 1e-16)
        else:
            time_value = np.maximum(mid_price - np.maximum(strikes - forward_price, 0.0), 1e-16)

        time_value = time_value / forward_price # / np.nansum(time_value)
        # w = np.diag(time_value)
        abs_m = np.reciprocal(np.maximum(np.abs(strikes - forward_price), 1e-8))
        abs_m = abs_m / np.nansum(abs_m)
        # mix with abs monenyness
        # w = np.diag(abs_m+time_value)
        w = np.diag(time_value)

    elif weight_type == WeightType.ABS_MONEYNESS:
        abs_m = np.maximum(np.abs(strikes - forward_price), 1e-8)
        w = np.diag(np.reciprocal(abs_m))

    elif weight_type == WeightType.BID_ASK_SPREAD:
        spread = (ask_price - bid_price)
        w = np.diag(np.reciprocal(spread))
    else:
        raise NotImplementedError(f"weight_type={weight_type}")
    return w


def get_aligned_bid_ask_prices(bid_ask_prices: pd.DataFrame) -> Tuple[pd.Series, pd.Series, pd.Series, pd.Series, pd.Series]:
    """
    align bid and ask prices and assigne the weight
    validity: 0: both are nans, 1: one is nan, 2: both are good
    """
    joint_prices = bid_ask_prices.sort_index()
    bid_prices, ask_prices = joint_prices.iloc[:, 0], joint_prices.iloc[:, 1]
    mid_prices = 0.5*(bid_prices + ask_prices)
    quote_validity = pd.Series(np.where(pd.isna(mid_prices) == False, 1, 0), index=mid_prices.index)
    bid_ask_spread = 0.5*(ask_prices-bid_prices)
    """
    # exclude prices where one quote is nan
    mid_price = mid_price.dropna()
    joint_prices = joint_prices.loc[mid_price.index, :]
    strikes = mid_price.index.to_numpy()
    bid_prices = joint_prices.iloc[:, 0].to_numpy()
    ask_prices = joint_prices.iloc[:, 1].to_numpy()
    mid_prices = pd.Series(0.5 * (bid_prices + ask_prices), index=strikes)
    bid_prices = pd.Series(bid_prices, index=strikes)
    ask_prices = pd.Series(ask_prices, index=strikes)
    """
    return mid_prices, quote_validity, bid_ask_spread, bid_prices, ask_prices


def infer_mark_call_put_price_with_qp_solver(call_bid_ask_prices: pd.DataFrame,
                                             put_bid_ask_prices: pd.DataFrame,
                                             forward_price: float,
                                             discfactor: float,
                                             eps: float = 1e-8,
                                             weight_type: WeightType = WeightType.TIME_VALUE,
                                             verbose: bool = True,
                                             is_add_bid_ask_constraint: bool = True,
                                             bid_ask_contraint_band: float = 0.99  # deflate / inflate
                                             ) -> Tuple[Optional[pd.Series], Optional[pd.Series]]:
    """
    solve qp problem to infer valid mark prices
    """
    # reindex at joint strikes
    joint_strikes = list(set(call_bid_ask_prices.index.to_list()) & set(put_bid_ask_prices.index.to_list()))
    call_bid_ask_prices = call_bid_ask_prices.reindex(index=joint_strikes).sort_index()
    put_bid_ask_prices = put_bid_ask_prices.reindex(index=joint_strikes).sort_index()
    joint_strikes = call_bid_ask_prices.index.to_numpy()

    # set mids and validity
    call_mid_price, call_validity, call_bid_ask_spread, call_bid_prices, call_ask_prices \
        = get_aligned_bid_ask_prices(bid_ask_prices=call_bid_ask_prices)
    put_mid_price, put_validity, put_bid_ask_spread, put_bid_prices, put_ask_prices \
        = get_aligned_bid_ask_prices(bid_ask_prices=put_bid_ask_prices)

    # for solver we need to fill nanns
    call_mid_price = call_mid_price.fillna(0.0).to_numpy()
    put_mid_price = put_mid_price.fillna(0.0).to_numpy()
    # these are used as trackers for weight
    is_call_available = call_validity.to_numpy(float)
    is_put_available = put_validity.to_numpy(float)
    is_call_put_available = is_call_available*is_put_available

    # set error weights
    weight_calls = compute_eror_weights(weight_type=weight_type,
                                        strikes=joint_strikes,
                                        bid_price=call_bid_prices.to_numpy(),
                                        ask_price=call_ask_prices.to_numpy(),
                                        forward_price=forward_price,
                                        is_calls=True)

    weight_puts = compute_eror_weights(weight_type=weight_type,
                                       strikes=joint_strikes,
                                       bid_price=put_bid_prices.to_numpy(),
                                       ask_price=put_ask_prices.to_numpy(),
                                       forward_price=forward_price,
                                       is_calls=False)
    # multiply by availability
    weight_calls = np.diag(weight_calls)
    weight_puts = np.diag(weight_puts)
    weights_call_put = np.diag(np.concatenate((weight_calls*is_call_available, weight_puts*is_put_available)))
    mid_price = np.concatenate((call_mid_price, put_mid_price))

    # set optimisation problem
    n = len(joint_strikes)
    n2 = 2*n
    z = cvx.Variable(n2, nonneg=True)
    D1, D2 = set_matrix_d1_d2(x=joint_strikes)
    Q = np.transpose(weights_call_put) @ weights_call_put
    q = - Q @ mid_price

    h1 = -eps*np.ones(n)
    h2 = -eps*np.ones(n)
    h1[0] = 1.0 - eps
    h2[-1] = 1.0 - eps

    constraints = [D1 @ z[:n] <= h1]
    constraints = constraints + [D1 @ z[n:] <= h2]

    # put call parity
    call_put_rhs = discfactor * (forward_price - joint_strikes)
    bid_ask_spreads = 0.5 * (call_bid_ask_spread.to_numpy() + put_bid_ask_spread.to_numpy())
    call_put_parity_constraints = []
    for idx, is_valid in enumerate(is_call_put_available):
        if is_valid > 0.0:  # put index is shifted by n
            call_put_parity_constraints += [-bid_ask_spreads[idx] <= z[idx] - z[n + idx] - call_put_rhs[idx]]
            call_put_parity_constraints += [bid_ask_spreads[idx] >= z[idx] - z[n + idx] - call_put_rhs[idx]]
    constraints = constraints + call_put_parity_constraints

    if is_add_bid_ask_constraint:
        call_constraints = []
        call_bids = np.minimum((1.0-bid_ask_contraint_band)*call_bid_prices.to_numpy(), 0.0)
        call_asks = (1.0 + bid_ask_contraint_band) * call_ask_prices.to_numpy()
        for idx, (is_call_available_, call_bid, call_ask) in enumerate(zip(is_call_available, call_bids, call_asks)):
            if is_call_available_ > 0:
                call_constraints += [z[idx] >= call_bid]
                call_constraints += [z[idx] <= call_ask]

        put_constraints = []
        put_bids = np.minimum((1.0-bid_ask_contraint_band)*put_bid_prices.to_numpy(), 0.0)
        put_asks = (1.0 + bid_ask_contraint_band) * put_ask_prices.to_numpy()
        for idx, (is_put_available_, put_bid, put_ask) in enumerate(zip(is_put_available, put_bids, put_asks)):
            if is_put_available_ > 0:  # puts are shifted by n
                put_constraints += [z[n+idx] >= put_bid]
                put_constraints += [z[n+idx] <= put_ask]

        constraints = constraints + call_constraints + put_constraints

    # start solver
    D2c = cvx.psd_wrap(np.transpose(D2) @ D2)
    D2p = cvx.psd_wrap(np.transpose(D2) @ D2)
    convexity_objective = 0.5*(cvx.quad_form(z[:n], D2c)+cvx.quad_form(z[n:], D2p))

    # total objective_fun
    objective_fun = 0.5*cvx.quad_form(z, Q) + q @ z # + convexity_objective
    objective = cvx.Minimize(objective_fun)
    problem = cvx.Problem(objective, constraints)
    try:
        kwargs = dict(max_iters=20000, feastol=1e-12, abstol=1e-12, reltol=1e-16)
        # problem.solve(solver=cvx.ECOS, verbose=verbose, **kwargs)
        problem.solve(solver=cvx.ECOS_BB, verbose=True, **kwargs)
        #problem.solve(verbose=verbose)
        # problem.solve()
        option_marks = z.value
    except cvx.error.SolverError:
        option_marks = None
    if option_marks is not None:
        print(f"puts: {np.logical_and(option_marks[n:]>=put_bid_prices.to_numpy(), option_marks[n:]<=put_ask_prices.to_numpy())} ")
        call_marks = pd.Series(np.maximum(option_marks[:n], 1e-16), index=joint_strikes, name='calls')
        put_marks = pd.Series(np.maximum(option_marks[n:], 1e-16), index=joint_strikes, name='puts')
    else:
        print(f"problem is not solved, try to decrease smootheness eps={eps}")
        call_marks, put_marks = None, None
    return call_marks, put_marks


# @njit
def compute_t_knots(x: np.ndarray, degree: int = 3) -> np.ndarray:
    """
    compute t_knots for b-spline
    default is degree = 3
    #
    """
    n = x.shape[0]
    n_knots = n + 4
    # compute nodes
    t_knots = np.zeros(n_knots)
    for n_ in np.arange(0, n-2):
        t_knots[n_+3] = 0.5*(x[n_+2]+x[n_+1])
        # t_knots[n_ + 2] = 0.5 * (x[n_ - 1] + x[n_])
        # t_knots[n_ + 2] = x[n_]
    t_knots[0] = t_knots[1] = t_knots[2] = x[0]
    t_knots[n+1] = t_knots[n+2] = t_knots[n+3] = x[n-1]
    print(x)
    print(t_knots)
    return t_knots


#@njit
def BB(x: float, i: int, t_knots: np.ndarray, degree: int = 3) -> float:
    """
    b-spline polynomial
    """
    if degree == 0:
        return 1.0 if t_knots[i] <= x < t_knots[i+1 ] else 0.0
    if t_knots[i + degree] == t_knots[i]:
        c1 = 0.0
    else:
        c1 = (x - t_knots[i]) / (t_knots[i + degree] - t_knots[i]) * B(x, i, t_knots, degree - 1)
    if t_knots[i + degree + 1] == t_knots[i + 1]:
        c2 = 0.0
    else:
        c2 = (t_knots[i + degree + 1] - x) / (t_knots[i + degree + 1] - t_knots[i + 1]) * B(x, i + 1, t_knots, degree - 1)
    return c1 + c2


#@njit
def B(x: float, i: int, t_knots: np.ndarray) -> float:
    """
    with uniform grid
    """
    h = t_knots[4]-t_knots[3]
    h2 = h*h
    h3 = h2*h
    if t_knots[i-1] <= x < t_knots[i]:
        b = np.power(x-t_knots[i-1], 3)
    elif t_knots[i] <= x < t_knots[i+1]:
        dx = x-t_knots[i]
        dx2 = dx*dx
        dx3 = dx2*dx
        b = -3.0*dx3 + 3.0*h*dx2 + 3.0*h2*dx+h3
    elif t_knots[i+1] <= x < t_knots[i+2]:
        dx = t_knots[i+2] - x
        dx2 = dx*dx
        dx3 = dx2*dx
        b = -3.0*dx3 + 3.0*h*dx2 + 3.0*h2*dx+h3
    elif t_knots[i+2] <= x < t_knots[i+3]:
        b = np.power(t_knots[i + 3] - x, 3)
    else:
        b = 0.0
    return b / (6.0*h3)


@njit
def B1(x: float, i: int, t_knots: np.ndarray) -> float:
    """
    with non-uniform grid
    """
    if t_knots[i-1] <= x < t_knots[i]:
        b = np.power(x-t_knots[i-1], 3) \
            / ((t_knots[i + 2] - t_knots[i - 1]) * (t_knots[i + 1] - t_knots[i - 1]) * (t_knots[i] - t_knots[i - 1]))
    elif t_knots[i] <= x < t_knots[i+1]:
        t1 = np.power(x-t_knots[i-1], 2) *(t_knots[i + 1]-x) \
             / ((t_knots[i + 2] - t_knots[i - 1]) * (t_knots[i + 1] - t_knots[i - 1]) * (t_knots[i+1] - t_knots[i]))
        t2 = (x-t_knots[i-1]) *(t_knots[i + 2]-x)*(x-t_knots[i]) \
             / ((t_knots[i + 2] - t_knots[i - 1]) * (t_knots[i + 2] - t_knots[i]) * (t_knots[i+1] - t_knots[i]))
        t3 = (t_knots[i+3] - x) * np.power(x-t_knots[i], 2) \
             / ((t_knots[i + 3] - t_knots[i]) * (t_knots[i + 2] - t_knots[i]) * (t_knots[i + 1] - t_knots[i]))
        b = t1 + t2 + t3
    elif t_knots[i+1] <= x < t_knots[i+2]:
        t1 = np.power(x-t_knots[i+2], 2) *(x-t_knots[i-1]) \
             / ((t_knots[i + 2] - t_knots[i - 1]) * (t_knots[i + 2] - t_knots[i]) * (t_knots[i+2] - t_knots[i+1]))
        t2 = (t_knots[i+3]-x) * (x-t_knots[i])*(t_knots[i+2]-x) \
             /( (t_knots[i + 3] - t_knots[i]) * (t_knots[i + 2] - t_knots[i]) * (t_knots[i+2] - t_knots[i+1]))
        t3 = (x-t_knots[i+1]) * np.power(t_knots[i+3]-x, 2) \
             / ((t_knots[i + 3] - t_knots[i]) * (t_knots[i + 3] - t_knots[i+1]) * (t_knots[i + 2] - t_knots[i+1]))
        b = t1 + t2 + t3
    elif t_knots[i + 2] <= x < t_knots[i + 3]:
        b = np.power(t_knots[i+3]-x, 3) \
            / ((t_knots[i + 3] - t_knots[i]) * (t_knots[i + 3] - t_knots[i + 1]) * (t_knots[i+3] - t_knots[i + 2]))
    else:
        b = 0.0
    return b


# @njit
def bspline_interpolation(x: np.ndarray, t_knots: np.ndarray, spline_coeffs: np.ndarray, degree: int = 3) -> np.ndarray:
    """
    given input array x
    t_knots and spline coefficients spline_coeffs
    compute spline interpolation
    """
    """
    n = len(t_knots) #- degree - 1
    # assert (n >= degree+1) and (len(spline_coeffs) >= n)
    y_spline = np.zeros_like(x)
    for idx, x_ in enumerate(x):
        sums = 0.0
        bb = np.zeros(n)
        for i in np.arange(2, n-4):
            bb[i] = B(x_, i=i, t_knots=t_knots)
            sums += spline_coeffs[i] * B(x_, i=i, t_knots=t_knots)
        print(f"idx={idx}: {bb}")
        y_spline[idx] = sums
    """
    spl = BSpline(t=t_knots, c=spline_coeffs, k=3)
    y_spline = np.zeros_like(x)
    for idx, x_ in enumerate(x):
        y_spline[idx] = spl(x_)
    return y_spline


def compute_p_matrix(x: np.ndarray, t_knots: np.ndarray, degree: int = 3) -> np.ndarray:
    n = x.shape[0]  # neew two extra points
    a = np.ones(n-1)
    b = 4.0*np.ones(n)
    c = np.ones(n-1)
    m = np.diag(a, -1) + np.diag(b, 0) + np.diag(c, 1)  # chape = n
    m[0, 0], m[0, 1], m[0, 2] = 1.0, 1.0, 1.0
    m[n-1, n-1], m[n-1, n-2] , m[n-1, n-3] = 1.0, 1.0, 1.0
    #m[0, 0], m[0, 1], m[0, 2] = 1.0, -2.0, 1.0
    #m[n-1, n-1], m[n-1, n-2] , m[n-1, n-3] = 1.0, -2.0, 1.0
    return m


def compute_b_spline(x: np.ndarray, y: np.ndarray, degree: int = 3, eps: float = 1e-3, is_monotonic: bool = True):
    """
    compute t_knots and spline coeffs
    """
    # t_knots = compute_t_knots(x=x, degree=degree)
    # compute b-spline matrix P[i,j]
    # x = np.concatenate((np.array([x[0]]), x, np.array([x[-1]])))
    #x = t_knots
    #y = 6.0*np.concatenate((np.array([0.0, 0.0*y[0]]), y, np.array([0.0*y[-1], 0.0])))
    # p = compute_p_matrix(x=x, t_knots=t_knots, degree=degree)

    bspl = make_interp_spline(x, y, k=3)
    p = bspl.design_matrix(x, bspl.t, k=3).toarray()
    t_knots = bspl.t
    print(t_knots)
    print(f"p=\n{p}")

    Q = np.transpose(p) @ p
    q = - np.transpose(p) @ y
    n = x.shape[0]
    z = cvx.Variable(n)
    # start solver
    objective_fun = 0.5*cvx.quad_form(z, Q) + q @ z
    objective = cvx.Minimize(objective_fun)

    G = set_matrix_g1(x=x)
    h = -eps*np.ones(n)
    #h[0] = 0.0
    #h[-1] = 0.0

    constraints = []
    if is_monotonic:
        constraints = constraints + [G @ z <= h]

    problem = cvx.Problem(objective, constraints)
    problem.solve(verbose=True)
    spline_coeffs = z.value
    # spline_coeffs = np.concatenate((np.array([2.0*spline_coeffs[0]-spline_coeffs[1]]), spline_coeffs, np.array([2.0*spline_coeffs[-1]-spline_coeffs[-2]])))

    print('spline_coeffs')
    print(spline_coeffs)

    return t_knots, spline_coeffs


@njit
def set_matrix_g1(x: np.ndarray) -> np.ndarray:
    """
    compute the matrix f partial derivatives without using dx
    loop is optimised with njit
    """
    nn = x.shape[0]
    g = np.zeros((nn, nn))
    for n in np.arange(nn):
        if n == 0:
            g[n, 0] = -1
            g[n, 1] = 1
        elif n == nn - 1:
            g[n, nn-2] = -1
            g[n, nn-1] = 1
        else:
            g[n, n] = -1
            g[n, n + 1] = 1
    return g


class UnitTests(Enum):
    RUN_B_SPLINE = 1
    COMPARE_B_SPLINES = 2
    NP_SPLINE = 3


def run_unit_test(unit_test: UnitTests):

    import matplotlib.pyplot as plt
    import qis as qis
    np.random.seed(5)

    x = np.linspace(0.1, 2.1, 25)
    x1 = np.linspace(0.1, 2.0, 100)
    # x1 = np.array([0.25, 0.41, 0.64, 0.71, 0.79, 0.81, 1.02, 1.23, 1.24, 1.46, 1.50, 1.53, 1.70, 1.9])
    # x1 = x
    noise = 0.001*np.random.normal(0.0, 1.0, size=x.shape[0])
    y = 1.0 / (1.0+np.sqrt(x))
    y_noise = y + noise
    yy = pd.concat([pd.Series(y, index=x, name='y'), pd.Series(y_noise, index=x, name='y_noise')], axis=1)

    if unit_test == UnitTests.RUN_B_SPLINE:

        t_knots, spline_coeffs = compute_b_spline(x=x, y=y_noise, is_monotonic=False)
        y_spline1 = bspline_interpolation(x=x1, t_knots=t_knots, spline_coeffs=spline_coeffs)
        y_spline1 = pd.Series(y_spline1, index=x1, name='y_spline')

        t_knots, spline_coeffs = compute_b_spline(x=x, y=y_noise, is_monotonic=True)
        y_spline2 = bspline_interpolation(x=x1, t_knots=t_knots, spline_coeffs=spline_coeffs)
        y_spline2 = pd.Series(y_spline2, index=x1, name='y_spline monotonic')

        df = pd.concat([yy, y_spline1, y_spline2], axis=1).sort_index()
        print(df)
        qis.plot_line(df=df)

    elif unit_test == UnitTests.COMPARE_B_SPLINES:
        t_knots = compute_t_knots(x=x)

        n = len(t_knots) - 3 - 1
        bb0 = np.zeros((n, n))
        bb1 = np.zeros((n, n))
        for idx, x_ in enumerate(x):
            for i in np.arange(0, n):
                bb0[idx, i] = B(x_, i=i, t_knots=t_knots)
                bb1[idx, i] = B1(x_, i=i, t_knots=t_knots)
        bb0 = pd.DataFrame(bb0, index=x)
        bb1 = pd.DataFrame(bb1, index=x)
        diff = bb0-bb1
        qis.plot_line(bb0, title='bb0')
        qis.plot_line(bb1, title='bb1')
        qis.plot_line(diff, title='diff')

    elif unit_test == UnitTests.NP_SPLINE:
        t_knots = compute_t_knots(x=x)
        # spl = BSpline(t=t_knots, c=None, k=3)
        #this = BSpline.design_matrix(x=x, t=t_knots, k=3, extrapolate=False)
        #print(this)
        bspl = make_interp_spline(x, y, k=3)
        design_matrix = bspl.design_matrix(x, bspl.t, k=3)
        print(design_matrix.toarray())


    plt.show()


if __name__ == '__main__':

    unit_test = UnitTests.RUN_B_SPLINE

    is_run_all_tests = False
    if is_run_all_tests:
        for unit_test in UnitTests:
            run_unit_test(unit_test=unit_test)
    else:
        run_unit_test(unit_test=unit_test)
