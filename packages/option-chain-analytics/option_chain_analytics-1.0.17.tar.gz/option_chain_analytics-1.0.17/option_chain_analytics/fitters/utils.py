
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import qis as qis
from dataclasses import dataclass
from typing import Tuple, Dict, Optional

import vanilla_option_pricers as bsm
from option_chain_analytics import SliceColumn
from option_chain_analytics.visuals.plots import plot_price_slice_fit, plot_vol_slice_fit_error_bar
from option_chain_analytics.utils.numerics import compute_pdf_from_prices


@dataclass
class SliceFitOutputs:
    forward: float
    discfactor: float
    call_mark_prices: pd.Series
    put_mark_prices: pd.Series
    calls_bid_iv: pd.Series
    calls_ask_iv: pd.Series
    calls_mark_iv : pd.Series
    puts_bid_iv: pd.Series
    puts_ask_iv: pd.Series
    puts_mark_iv: pd.Series

    def get_vol_dicts(self,
                      joint_strikes: Optional[pd.Index] = None
                      ) -> Tuple[Dict[str, pd.Series], ...]:

        calls_bid_iv = self.calls_bid_iv
        calls_ask_iv = self.calls_ask_iv
        calls_mark_iv = self.calls_mark_iv

        if joint_strikes is not None:
            calls_bid_iv = calls_bid_iv[joint_strikes].dropna()
            calls_ask_iv = calls_ask_iv[joint_strikes].dropna()
            calls_mark_iv = calls_mark_iv[joint_strikes].dropna()

        puts_bid_iv = self.puts_bid_iv
        puts_ask_iv = self.puts_ask_iv
        puts_mark_iv = self.puts_mark_iv
        if joint_strikes is not None:
            puts_bid_iv = puts_bid_iv[joint_strikes].dropna()
            puts_ask_iv = puts_ask_iv[joint_strikes].dropna()
            puts_mark_iv = puts_mark_iv[joint_strikes].dropna()

        bid_vols = {'call': calls_bid_iv,
                    'put': puts_bid_iv}
        ask_vols = {'call': calls_ask_iv,
                    'put': puts_ask_iv}
        model_vols = {'call': calls_mark_iv,
                      'put': puts_mark_iv}
        return bid_vols, ask_vols, model_vols


def imply_bid_ask_mark_vols(strikes: np.ndarray,
                            bid_prices: np.ndarray,
                            ask_prices: np.ndarray,
                            mark_prices: np.ndarray,
                            ttm: float,
                            forward: float,
                            discfactor: float,
                            optiontype: str = 'C'
                            ) -> Tuple[pd.Series, pd.Series, pd.Series]:

    bid_iv = bsm.infer_bsm_ivols_from_model_slice_prices(ttm=ttm, forward=forward,
                                                         strikes=strikes,
                                                         optiontypes=np.full(strikes.shape, optiontype),
                                                         model_prices=bid_prices,
                                                         discfactor=discfactor)
    ask_iv = bsm.infer_bsm_ivols_from_model_slice_prices(ttm=ttm, forward=forward,
                                                         strikes=strikes,
                                                         optiontypes=np.full(strikes.shape, optiontype),
                                                         model_prices=ask_prices,
                                                         discfactor=discfactor)
    mark_iv = bsm.infer_bsm_ivols_from_model_slice_prices(ttm=ttm, forward=forward,
                                                          strikes=strikes,
                                                          optiontypes=np.full(strikes.shape, optiontype),
                                                          model_prices=mark_prices,
                                                          discfactor=discfactor)
    bid_iv = pd.Series(bid_iv, index=strikes, name=SliceColumn.BID_IV.value)
    ask_iv = pd.Series(ask_iv, index=strikes,  name=SliceColumn.ASK_IV.value)
    mark_iv = pd.Series(mark_iv, index=strikes,  name=SliceColumn.MARK_IV.value)
    return bid_iv, ask_iv, mark_iv


def compute_bounded_delta_strikes(forward: float, ttm: float, strike: np.ndarray, vol: np.ndarray,
                                  discfactor: float,
                                  optiontype: str = 'C',
                                  bounds: Tuple[float, float] = (0.05, 0.95)
                                  ) -> pd.Series:
    delta = bsm.compute_bsm_vanilla_delta_vector(forward=forward,
                                                 ttm=ttm,
                                                 strike=strike,
                                                 vol=vol,
                                                 optiontype=optiontype,
                                                 discfactor=discfactor)
    delta = pd.Series(delta, index=strike)
    if optiontype == 'C':
        bounded_deltas = delta.loc[np.logical_and(delta > bounds[0], delta < bounds[1])]
    else:
        bounded_deltas = delta.loc[np.logical_and(delta < -bounds[0], delta > -bounds[1])]
    return bounded_deltas


def plot_slice_fits(slice_df: pd.DataFrame,
                    slice_fit_outputs: SliceFitOutputs,
                    expiry: str = None,
                    bounds: Optional[Tuple[float, float]] = (0.01, 0.95)
                    ) -> plt.Figure:

    if bounds is not None:
        call_bounded_deltas = compute_bounded_delta_strikes(forward=slice_fit_outputs.forward,
                                                            ttm=slice_df[SliceColumn.TTM].iloc[0],
                                                            strike=slice_fit_outputs.calls_mark_iv.index.to_numpy(),
                                                            vol=slice_fit_outputs.calls_mark_iv.to_numpy(),
                                                            discfactor=slice_fit_outputs.discfactor,
                                                            optiontype='C',
                                                            bounds=bounds)

        put_bounded_deltas = compute_bounded_delta_strikes(forward=slice_fit_outputs.forward,
                                                           ttm=slice_df[SliceColumn.TTM].iloc[0],
                                                           strike=slice_fit_outputs.puts_mark_iv.index.to_numpy(),
                                                           vol=slice_fit_outputs.puts_mark_iv.to_numpy(),
                                                           optiontype='P', discfactor=slice_fit_outputs.discfactor,
                                                           bounds=bounds)
        joint_strikes = pd.Index(call_bounded_deltas.index).union(pd.Index(put_bounded_deltas.index)).sort_values()
        # joint_strikes = joint_strikes.drop_duplicates().sort_values()
    else:
        joint_strikes = None

    bid_vols, ask_vols, model_vols = slice_fit_outputs.get_vol_dicts(joint_strikes=joint_strikes)
    bid_price = slice_df[SliceColumn.BID_PRICE.value]
    ask_price = slice_df[SliceColumn.ASK_PRICE.value]
    model_prices = pd.concat([slice_fit_outputs.call_mark_prices.rename('Calls'),
                              slice_fit_outputs.put_mark_prices.rename('Puts')], axis=1)
    if joint_strikes is not None:
        bid_price = bid_price.loc[np.logical_and(bid_price.index>=joint_strikes[0], bid_price.index<=joint_strikes[-1])]
        ask_price = ask_price.loc[np.logical_and(ask_price.index>=joint_strikes[0], ask_price.index<=joint_strikes[-1])]
        model_prices = model_prices.loc[np.logical_and(model_prices.index>=joint_strikes[0], model_prices.index<=joint_strikes[-1]), :]

    with sns.axes_style("darkgrid"):
        fig, axs = plt.subplots(2, 2, figsize=(14, 7), tight_layout=True)
        plot_price_slice_fit(bid_price=bid_price,
                             ask_price=ask_price,
                             model_prices=model_prices,
                             is_log=True,
                             title='Prices',
                             ax=axs[0, 0])
        plot_vol_slice_fit_error_bar(bid_vols=bid_vols, ask_vols=ask_vols, model_vols=model_vols,
                                     title='Volatilities',
                                     ax=axs[1, 0])
        # pdfs
        call_cpdf, call_pdf = compute_pdf_from_prices(option_prices=slice_fit_outputs.call_mark_prices, is_call=True)
        put_cpdf, put_pdf = compute_pdf_from_prices(option_prices=slice_fit_outputs.put_mark_prices, is_call=False)
        cpdfs = pd.concat([call_cpdf.rename('call'), put_cpdf.rename('put')], axis=1)
        pdfs = pd.concat([call_pdf.rename('call'), put_pdf.rename('put')], axis=1)
        if joint_strikes is not None:
            cpdfs = cpdfs.loc[joint_strikes, :]
            pdfs = pdfs.loc[joint_strikes, :]

        qis.plot_line(df=cpdfs, title='cpdfs', ax=axs[0, 1])
        qis.plot_line(df=pdfs, title='pdfs', ax=axs[1, 1])

        if expiry is not None:
            title = f"{expiry}: forward={slice_fit_outputs.forward:0.2f}, discfactor={slice_fit_outputs.discfactor:0.2f}"
        else:
            title = f"forward={slice_fit_outputs.forward:0.2f}, discfactor={slice_fit_outputs.discfactor:0.2f}"

        qis.set_suptitle(fig, title=title)

    return fig
