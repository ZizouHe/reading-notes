import numpy as np
import xarray as xr
import math

def _ewm_ma_halflife(x: xr.DataArray, dim: str = "D", half_life: float = 10.0, mode='mean') -> xr.DataArray:
    """Apply pandas ewm(mean) along a single dimension via xarray.apply_ufunc."""
    def _ewm_1d(a, mode):
        s = pd.Series(a)
        ewm_obj = s.ewm(halflife=half_life, adjust=False, min_periods=1)
        if mode == 'mean':
            return ewm_obj.mean().to_numpy()
        if mode == 'std':
            return ewm_obj.std().to_numpy()

    return xr.apply_ufunc(
        _ewm_1d, x,
        input_core_dims=[[dim]],
        output_core_dims=[[dim]],
        vectorize=True,
        dask="parallelized",
        output_dtypes=[np.float64],
    )

def compute_diff_std_volb(
    da: xr.DataArray,
    half_life: int=20,
):
    for v in ("locVol","numTrade"):
        if v not in da.coords["V1"].values:
            raise ValueError(f"Missing required variable '{v}' in V1")

    v_locVol = da.sel(V1="locVol")
    v_numTr  = da.sel(V1="numTrade")

    volb = divide_safe(v_locVol, v_numTr)

    diff_raw = volb.diff(dim="E", label="upper")
    diff_full = diff_raw.reindex(E=volb["E"])
    day_mean_volb = volb.mean("E", skipna=True)
    day_mean_volb_b = day_mean_volb.broadcast_like(volb)
    norm_abs_diff = (diff_full.abs() / day_mean_volb_b).astype("float64")
    diff_std_day = norm_abs_diff.std("E", skipna=True)
    #diff_std_day = norm_abs_diff.mean("E", skipna=True)
    #fac_trailing = diff_std_day.rolling(D=half_life, min_periods=1).mean().isel(D=[-1])
    fac_trailing = _ewm_ma_halflife(diff_std_day, dim="D", half_life=half_life).isel(D=[-1])
    f_b = fac_trailing.broadcast_like(volb.D=[-1])
    out = xr.concat([f_b], dim="V1").assign_coords(V1=["factor_diff_std_volb"])
    out = out.transpose("S","D","E","V1")
    return out

def compute_hf_upvol_share(
    da: xr.DataArray,
    ret_var: str = "ret",
    half_life: int = 20,
) -> xr.DataArray:
    if ret_var not in da.coords["V1"].values:
        raise ValueError(f"Variable '{ret_var}' not found in V1")

    ret = da.sel(V1=ret_var)
    num_day = (ret.clip(min=0) ** 2).sum("E", skipna=True)
    den_day = (ret ** 2).sum("E", skipna=True)
    ratio_day = divide_safe(num_day, den_day)
    ratio_ema = _ewm_ma_halflife(ratio_day, dim="D", half_life=half_life)

    ratio_last = ratio_ema.isel(D=[-1])
    factor_last = ratio_last.broadcast_like(ret.isel(D=[-1]))

    out_list = [factor_last]

    out = xr.concat(out_list, dim="V1").assign_coords(V1=["hf_upvol_share"])
    out = out.transpose("S","D","E","V1")
    return -1*out

def compute_cv_illiq(
    da: xr.DataArray,
    ret_var: str = "ret",
    vol_var: str = "locVol",
    half_life: float = 20,
) -> xr.DataArray:
    for v in (ret_var, vol_var):
        if v not in da.coords["V1"].values:
            raise ValueError(f"Variable '{v}' not found in V1")

    ret  = da.sel(V1=ret_var)
    amount   = da.sel(V1=vol_var)
    amount = close * vol
    illiq_min = divide_safe(ret.abs(), amount)
    illiq_day = illiq_min.mean("E", skipna=True)
    mu_ewm  = _ewm_ma_halflife(illiq_day, dim="D", half_life=half_life, mode='mean')
    std_ewm = _ewm_ma_halflife(illiq_day, dim="D", half_life=half_life, mode='std')
    cv_series = divide_safe(std_ewm, mu_ewm)

    factor_last = cv_series.isel(D=[-1]).broadcast_like(ret.isel(D=[-1]))
    out = xr.concat([factor_last], dim="V1").assign_coords(V1=['cv_illiq'])
    out = out.transpose("S","D","E","V1")
    return out

def compute_vol_spike_count(
    da: xr.DataArray,
    vol_var: str = "volume",
    k_std: float = 1.0,
    half_life: float = 10.0,
) -> xr.DataArray:
    if vol_var not in da.coords["V1"].values:
        raise ValueError(f"Variable '{vol_var}' not found in V1")

    vol = da.sel(V1=vol_var)

    day_mean = vol.mean("E", skipna=True)                  # S x D
    day_std  = vol.std("E", skipna=True)                   # S x D
    thr = (day_mean + k_std * day_std).broadcast_like(vol) # S x D x E

    flagged = (vol > thr).fillna(False)                    # bool S x D x E

    prev_flagged = flagged.shift(E=1, fill_value=False)
    keep = flagged & (~prev_flagged)                       # bool S x D x E

    count_day = keep.sum("E").astype("float64")            # S x D
    count_ema = _ewm_ma_halflife(count_day, dim="D", half_life=half_life, mode="mean")  # S x D

    factor_last = count_ema.isel(D=[-1]).broadcast_like(vol.isel(D=[-1]))       # S x 1 x E

    out = xr.concat([factor_last], dim="V1").assign_coords(V1=[vol_spike_count])
    out = out.transpose("S","D","E","V1")
    return out


def compute_price_impact_bias(
    da: xr.DataArray,
    ret_var: str = "ret",
    buy_var: str = "locVolBuy",
    sell_var: str = "locVolSell",
    amount_var: str = "locVol",
    half_life: float = 10.0,
) -> xr.DataArray:
    for v in (ret_var, "locVolBuy", "locVolSell", "locVol"):
        if v not in da.coords["V1"].values:
            raise ValueError(f"Variable '{v}' not found in V1")

    ret   = da.sel(V1=ret_var)
    buy   = da.sel(V1="locVolBuy")
    sell  = da.sel(V1="locVolSell")
    amount = da.sel(V1="locVol")

    moneyflow = buy - sell
    mf = divide_safe(moneyflow, amount)

    valid = xr.ufuncs.isfinite(mf) & xr.ufuncs.isfinite(ret)
    mf = xr.where(valid, mf, np.nan)
    ret = xr.where(valid, ret, np.nan)

    up_mask   = ret >= 0
    down_mask = ~up_mask

    mf_up   = xr.where(up_mask, mf, np.nan)
    mf_down = xr.where(down_mask, mf, np.nan)

    num_up  = (mf_up * ret).sum("E", skipna=True)          # S x D
    den_up  = (mf_up ** 2).sum("E", skipna=True)           # S x D
    gamma_up = divide_safe(num_up, den_up)                 # S x D

    num_dn  = (mf_down * ret).sum("E", skipna=True)
    den_dn  = (mf_down ** 2).sum("E", skipna=True)
    gamma_down = divide_safe(num_dn, den_dn)               # S x D

    bias_day = divide_safe(gamma_up - gamma_down, gamma_up + gamma_down)  # S x D
    bias_ema = _ewm_ma_halflife(bias_day, dim="D", half_life=half_life, mode="mean")  # S x D

    factor_last = bias_ema.isel(D=[-1]).broadcast_like(ret.isel(D=[-1]))  # S x 1 x E

    out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array(["price_impact_bias"]))
    out = out.transpose("S","D","E","V1")
    return out


def compute_pv_corr_family(
    da: xr.DataArray,
    price_var: str = "robust",
    vol_var: str = "locVol",
    half_life: float = 10.0,
    mode: str = "avg",   # 'avg' | 'std' | 'trend'
) -> xr.DataArray:
    ## todo: mean condi ret
    if mode not in {"avg", "std", "trend"}:
        raise ValueError("mode must be one of {'avg','std','trend'}")
    for v in (price_var, vol_var):
        if v not in da.coords["V1"].values:
            raise ValueError(f"Variable '{v}' not found in V1")

    price = da.sel(V1=price_var)  # S x D x E
    vol   = da.sel(V1=vol_var)    # S x D x E

    p_mean = price.mean("E", skipna=True)
    v_mean = vol.mean("E",   skipna=True)
    p_dm   = price - p_mean
    v_dm   = vol   - v_mean
    p_std  = price.std("E", skipna=True)
    v_std  = vol.std("E",   skipna=True)

    z_p = divide_safe(p_dm, p_std)
    z_v = divide_safe(v_dm, v_std)
    corr_day = (z_p * z_v).mean("E", skipna=True)  # S x D

    if mode == "avg":
        fac_series = _ewm_ma_halflife(corr_day, dim="D", half_life=half_life, mode="mean")  # S x D
        out_name = "pv_corr_avg"

    elif mode == "std":
        fac_series = -ewm_ma_halflife(corr_day, dim="D", half_life=half_life, mode="std")   # S x D
        out_name = "pv_corr_std"

    else:  # mode == 'trend'
        nD = corr_day.sizes["D"]
        ages = xr.DataArray(np.arange(nD)[::-1], dims=["D"], coords={"D": corr_day["D"]}).astype("float64")
        w = (0.5 ** (ages / float(half_life))).astype("float64")   # D
        wB = w.broadcast_like(corr_day)                            # S x D

        x = xr.DataArray(np.arange(nD), dims=["D"], coords={"D": corr_day["D"]}).astype("float64")
        xB = x.broadcast_like(corr_day)                            # S x D

        wsum = w.sum("D", skipna=True)                             # scalar
        xbar = (w * x).sum("D", skipna=True) / wsum                # scalar
        x_center = xB - xbar                                       # S x D (broadcasted)

        y = corr_day                                               # S x D
        ybar = (wB * y).sum("D", skipna=True) / wsum               # S
        y_center = y - ybar.broadcast_like(y)                      # S x D

        num = (wB * x_center * y_center).sum("D", skipna=True)     # S
        den = (wB * x_center * x_center).sum("D", skipna=True)     # S
        fac_series = divide_safe(num, den).expand_dims(D=[da["D"].values[-1]])  # S x 1 (treat as a day)
        out_name = "pv_corr_trend"

    factor_last = fac_series.isel(D=[-1]).broadcast_like(vol.isel(D=[-1]))  # S x 1 x E
    out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array([out_name]))
    return -1*out.transpose("S","D","E","V1")


def compute_rsj_asymmetry(
    da: xr.DataArray,
    ret_var: str = "ret",
    half_life: float = 10.0,
) -> xr.DataArray:
    if ret_var not in da.coords["V1"].values:
        raise ValueError(f"Variable '{ret_var}' not found in V1")

    r = da.sel(V1=ret_var)                          # S x D x E
    r2 = r * r
    rv_all  = r2.sum("E", skipna=True)              # S x D
    rv_up   = xr.where(r > 0, r2, 0.0).sum("E", skipna=True)   # S x D
    rv_down = xr.where(r < 0, r2, 0.0).sum("E", skipna=True)   # S x D

    rsj_day = divide_safe(rv_up - rv_down, rv_all)  # S x D
    rsj_ema = _ewm_ma_halflife(rsj_day, dim="D", half_life=half_life, mode="mean")  # S x D

    factor_last = rsj_ema.isel(D=[-1]).broadcast_like(r.isel(D=[-1]))  # S x 1 x E
    out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array(["rsj_asym"]))
    return -1*out.transpose("S","D","E","V1")

def compute_ambiguity_amount_ratio(
    da: xr.DataArray,
    ret_var: str = "ret",
    half_life: float = 10.0,
    mode: str = "amount",         # 'amount' | 'volume' | 'spread'
) -> xr.DataArray:
    if mode not in {"amount", "volume", "spread"}:
        raise ValueError("mode must be one of {'amount','volume','spread'}")
    for v in (ret_var, "locVol", "volume"):
        if v not in da.coords["V1"].values:
            raise ValueError(f"Variable '{v}' not found in V1")

    r   = da.sel(V1=ret_var)        # S x D x E
    amt = da.sel(V1="locVol")     # S x D x E  (Amount ≡ locVol)
    vol = da.sel(V1="volume")    # S x D x E  (Quantity)

    sigma = r.rolling(E=5, min_periods=5).std()
    amb   = sigma.rolling(E=5, min_periods=5).std()

    amb_day_mean = amb.mean("E", skipna=True).broadcast_like(amb)
    fog = amb > amb_day_mean

    def _daily_ratio(x: xr.DataArray) -> xr.DataArray:
        fog_mean = x.where(fog).mean("E", skipna=True)  # S x D
        all_mean = x.mean("E", skipna=True)             # S x D
        return divide_safe(fog_mean, all_mean)          # S x D

    if mode in {"amount", "spread"}:
        ratio_amt_day = _daily_ratio(amt)               # S x D
    if mode in {"volume", "spread"}:
        ratio_vol_day = _daily_ratio(vol)              # S x D

    if mode == "amount":
        series_day = ratio_amt_day
        fac_name = "amb_amount_ratio"
    elif mode == "volume":
        series_day = ratio_vol_day
        fac_name = "amb_volume_ratio"
    else:
        spread_day = ratio_amt_day - ratio_vol_day      # S x D
        std10 = spread_day.rolling(D=half_life, min_periods=1).std()  # S x D
        neg_mask = spread_day < 0
        adjusted = xr.where(neg_mask, divide_safe(spread_day, std10), spread_day)  # S x D

        s1 = spread_day.where(spread_day < 0).fillna(0.0).sum("S", skipna=True)   # D
        s2 = adjusted.where(adjusted < 0).fillna(0.0).sum("S", skipna=True)       # D
        scale = divide_safe(s1, s2)                                               # D
        scaleB = scale.broadcast_like(adjusted)                                   # S x D
        adjusted = xr.where(adjusted < 0, adjusted * scaleB, adjusted)            # S x D
        series_day = adjusted
        fac_name = "amb_price_spread_adj"

    ema_mean = _ewm_ma_halflife(series_day, dim="D", half_life=half_life, mode="mean")  # S x D
    factor_last = ema_mean.isel(D=[-1]).broadcast_like(vol.isel(D=[-1]))  # S x 1 x E
    out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array([fac_name]))
    return -1*out.transpose("S","D","E","V1")

def compute_arpp(
    da: xr.DataArray,
    half_life: float = 10.0,
) -> xr.DataArray:
    for v in ("robust", "high", "low"):
        if v not in da.coords["V1"].values:
            raise ValueError(f"Variable '{v}' not found in V1")

    price = da.sel(V1="robust")
    high  = da.sel(V1="high")
    low   = da.sel(V1="low")

    twap_day = price.mean("E", skipna=True)
    high_day = high.max("E", skipna=True)
    low_day  = low.min("E", skipna=True)

    denom = high_day - low_day
    arpp_day = divide_safe(twap_day - low_day, denom)
    arpp_day = xr.where(np.isfinite(arpp_day), arpp_day.clip(0.0, 1.0), np.nan)
    arpp_ema = _ewm_ma_halflife(arpp_day, dim="D", half_life=half_life, mode="mean")
    factor_last = arpp_ema.isel(D=[-1]).broadcast_like(price.isel(D=[-1]))
    out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array(["arpp"]))
    return out.transpose("S","D","E","V1")


def compute_illiq_shortcut(
    da: xr.DataArray,
    half_life: float = 10.0,
) -> xr.DataArray:
    for v in ("open", "robust", "high", "low", "locVol"):
        if v not in da.coords["V1"].values:
            raise ValueError(f"Variable '{v}' not found in V1")

    o = da.sel(V1="open")       # S x D x E
    c = da.sel(V1="robust")
    h = da.sel(V1="high")
    l = da.sel(V1="low")
    amt = da.sel(V1="locVol")   # S x D x E

    shortcut = 2.0 * (h - l) - (c - o).abs()                       # S x D x E
    ratio = divide_safe(shortcut, amt)                              # S x D x E
    illiq_day = ratio.sum("E", skipna=True)                         # S x D
    illiq_ema = _ewm_ma_halflife(illiq_day, dim="D", half_life=half_life, mode="mean")  # S x D
    factor_last = illiq_ema.isel(D=[-1]).broadcast_like(c.isel(D=[-1]))  # S x 1 x E

    out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array(["illiq_shortcut"]))
    return out.transpose("S","D","E","V1")

def compute_cdpp(
    da: xr.DataArray,
    price_var: str = "robust",
    half_life: float = 10.0,
) -> xr.DataArray:
    if "robust" not in da.coords["V1"].values:
        raise ValueError(f"Variable '{"robust"}' not found in V1")

    p = da.sel(V1="robust")
    dP = p.diff("E")
    dP = dP.reindex(E=p["E"])
    dP_lead = dP.shift(E=-1)
    pos = dP > 0
    neg = dP < 0

    dP_pos = xr.where(pos, dP, np.nan)
    dP_lead_pos = xr.where(pos, dP_lead, np.nan)
    corr_pos_day = xr.corr(dP_pos, dP_lead_pos, dim="E")   # S x D

    dP_neg = xr.where(neg, dP, np.nan)
    dP_lead_neg = xr.where(neg, dP_lead, np.nan)
    corr_neg_day = xr.corr(dP_neg, dP_lead_neg, dim="E")   # S x D

    ema_pos = _ewm_ma_halflife(corr_pos_day, dim="D", half_life=half_life, mode="mean")
    ema_neg = _ewm_ma_halflife(corr_neg_day, dim="D", half_life=half_life, mode="mean")

    mu_p = ema_pos.isel(D=-1).mean("S", skipna=True)
    sd_p = ema_pos.isel(D=-1).std("S",  skipna=True)
    z_p = divide_safe(ema_pos.isel(D=-1) - mu_p, sd_p)

    mu_n = ema_neg.isel(D=-1).mean("S", skipna=True)
    sd_n = ema_neg.isel(D=-1).std("S",  skipna=True)
    z_n = divide_safe(ema_neg.isel(D=-1) - mu_n, sd_n)

    combined = 0.5 * (z_p + z_n)                       # S
    series_last = combined.expand_dims(D=[da["D"].values[-1]])  # S x 1

    factor_last = series_last.broadcast_like(p.isel(D=[-1]))    # S x 1 x E
    out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array(["cdpp"]))
    return out.transpose("S","D","E","V1")


def compute_ncskew(
    da: xr.DataArray,
    ret_var: str = "ret",
    half_life: float = 10.0,
) -> xr.DataArray:
    if ret_var not in da.coords["V1"].values:
        raise ValueError(f"Variable '{ret_var}' not found in V1")

    r_min = da.sel(V1=ret_var)                         # S x D x E
    r_day = (1.0 + r_min).prod("E", skipna=True) - 1.0 # S x D

    mu = _ewm_ma_halflife(r_day, dim="D", half_life=half_life, mode="mean")  # S x D
    sigma = _ewm_ma_halflife(r_day, dim="D", half_life=half_life, mode="std")# S x D

    c = r_day - mu
    m3_ewm = _ewm_ma_halflife(c**3, dim="D", half_life=half_life, mode="mean")  # S x D

    denom = sigma ** 3
    ncs = - divide_safe(m3_ewm, denom)                 # S x D

    factor_last = ncs.isel(D=[-1]).broadcast_like(r_min.isel(D=[-1]))  # S x 1 x E
    out = xr.concat([factor_last], dim="V1").assign_coords(V1=np.array(["ncskew_ewm"]))
    return out.transpose("S","D","E","V1")


def compute_volume_support_pb(
    da: xr.DataArray,
    half_life: float = 10.0,
    mode: str = "b"
) -> xr.DataArray:
    for v in ("robust", "volume", "high", "low"):
        if v not in da.coords["V1"].values:
            raise ValueError(f"Variable '{v}' not found in V1")

    price = da.sel(V1="robust")  # S x D x E
    vol   = da.sel(V1="volume") # S x D x E
    high  = da.sel(V1="high")   # S x D x E
    low   = da.sel(V1="low")    # S x D x E

    high_day = high.max("E", skipna=True)   # S x D
    low_day  = low.min("E", skipna=True)    # S x D
    close_day  = price.isel(E=-1)    # S x D

    def _vsa_bounds_1d(p_arr: np.ndarray, v_arr: np.ndarray):
        mask = np.isfinite(p_arr) & np.isfinite(v_arr) & (v_arr > 0)
        if mask.sum() == 0:
            return np.nan, np.nan
        df = pd.DataFrame({"p": p_arr[mask], "v": v_arr[mask]})
        agg = df.groupby("p", sort=True)["v"].sum()
        total = float(agg.sum())
        if total <= 0:
            return np.nan, np.nan

        vmax = agg.max()
        vsp = agg[agg == vmax].index.values.mean()

        uniq_prices = agg.index.values
        vols = agg.values
        dist = np.abs(uniq_prices - vsp)
        order = np.lexsort((-vols, dist))

        cum = 0.0
        sel = np.zeros_like(order, dtype=bool)
        for idx in order:
            sel[idx] = True
            cum += vols[idx]
            if cum >= 0.5 * total:
                break
        chosen_prices = uniq_prices[sel]
        return float(chosen_prices.min()), float(chosen_prices.max())

    vsa_low, vsa_high = xr.apply_ufunc(
        _vsa_bounds_1d,
        price, vol,
        input_core_dims=[["E"], ["E"]],
        output_core_dims=[[], []],
        vectorize=True,
        dask="parallelized",
        output_dtypes=[np.float64, np.float64],
    )

    if mode == "p":
        vsa_low2max_day  = divide_safe(high_day - vsa_low, high_day)
        vsa_ema = _ewm_ma_halflife(vsa_low2max_day,  dim="D", half_life=half_life, mode="mean")
        out_name = "vsa_p_low2max"
    elif mode == "b":
        vsa_high2min_day = divide_safe(vsa_high - low_day, low_day)
        vsa_ema = _ewm_ma_halflife(vsa_high2min_day, dim="D", half_life=half_life, mode="mean")
        out_name = "vsa_b_high2min"
    elif mode == 'r':
        vsa_high2min_day = divide_safe(vsa_low - close_day, close_day)
        vsa_ema = _ewm_ma_halflife(vsa_high2min_day, dim="D", half_life=half_life, mode="mean")
        out_name =

    f_last = vsa_ema.isel(D=[-1]).broadcast_like(vol.isel(D=[-1]))  # S x 1 x E

    out = xr.concat([f_last], dim="V1").assign_coords(V1=[out_name])
    return out.transpose("S","D","E","V1")


def _mu_abs_normal(q: float) -> float:
    """E|Z|^q for Z~N(0,1) = 2^{q/2} / sqrt(pi) * Gamma((1+q)/2)."""
    return (2.0 ** (q / 2.0)) / math.sqrt(math.pi) * math.gamma((1.0 + q) / 2.0)

def compute_jump_volatility_family(
    da: xr.DataArray,
    ret_var: str = "ret",
    half_life: float = 10.0,
    alpha: float = 4.0,
) -> xr.DataArray:
    if ret_var not in da.coords["V1"].values:
        raise ValueError(f"Variable '{ret_var}' not found in V1")

    r = da.sel(V1=ret_var)  # S x D x E

    rs_plus  = xr.where(r > 0, r*r, 0.0).sum("E", skipna=True)   # S x D
    rs_minus = xr.where(r < 0, r*r, 0.0).sum("E", skipna=True)   # S x D

    mu23 = _mu_abs_normal(2.0/3.0)
    ar = r.abs() ** (2.0/3.0)
    tp = (ar * ar.shift(E=1) * ar.shift(E=2)).sum("E", skipna=True)  # S x D
    iv_hat = tp / (mu23 ** 3)

    rv_all = (r*r).sum("E", skipna=True)                           # S x D
    nbar = r.count("E")                                            # S x D  (per-day valid bar count)
    delta_n = divide_safe(1.0, nbar)                               # S x D

    rvjp = xr.ufuncs.maximum(rs_plus - 0.5 * iv_hat, 0.0)          # S x D
    rvjn = xr.ufuncs.maximum(rs_minus - 0.5 * iv_hat, 0.0)         # S x D
    srvj = rvjp - rvjn                                             # S x D

    gamma = alpha * (delta_n ** 0.49) * xr.ufuncs.sqrt(iv_hat)     # S x D
    gamma_b = gamma.broadcast_like(r)                               # S x D x E

    sum_up_big   = xr.where(r >  gamma_b, r*r, 0.0).sum("E", skipna=True)  # S x D
    sum_down_big = xr.where(r < -gamma_b, r*r, 0.0).sum("E", skipna=True)  # S x D

    rvljp = xr.ufuncs.minimum(rvjp, sum_up_big)                    # S x D
    rvljn = xr.ufuncs.minimum(rvjn, sum_down_big)                  # S x D
    rvsjp = rvjp - rvljp                                           # S x D
    rvsjn = rvjn - rvljn                                           # S x D
    srvlj = rvljp - rvljn                                          # S x D
    srvsj = rvsjp - rvsjn                                          # S x D

    abs_r = r.abs()
    W = xr.ufuncs.maximum(divide_safe(abs_r, gamma_b) - 1.0, 0.0).sum("E", skipna=True)  # S x D
    num_tsrjv = _ewm_ma_halflife(W * srvj, dim="D", half_life=half_life, mode="mean")    # S x D
    den_tsrjv = _ewm_ma_halflife(W,         dim="D", half_life=half_life, mode="mean")   # S x D
    tsrjv = divide_safe(num_tsrjv, den_tsrjv)                                            # S x D

    series_map = {
        "rvjp":  _ewm_ma_halflife(rvjp,  dim="D", half_life=half_life, mode="mean"),
        "rvjn":  _ewm_ma_halflife(rvjn,  dim="D", half_life=half_life, mode="mean"),
        "srvj":  _ewm_ma_halflife(srvj,  dim="D", half_life=half_life, mode="mean"),
        "rvljp": _ewm_ma_halflife(rvljp, dim="D", half_life=half_life, mode="mean"),
        "rvljn": _ewm_ma_halflife(rvljn, dim="D", half_life=half_life, mode="mean"),
        "rvsjp": _ewm_ma_halflife(rvsjp, dim="D", half_life=half_life, mode="mean"),
        "rvsjn": _ewm_ma_halflife(rvsjn, dim="D", half_life=half_life, mode="mean"),
        "srvlj": _ewm_ma_halflife(srvlj, dim="D", half_life=half_life, mode="mean"),
        "srvsj": _ewm_ma_halflife(srvsj, dim="D", half_life=half_life, mode="mean"),
        "tsrjv": tsrjv,
    }

    out = xr.concat(list(series_map.values()), dim="V1").assign_coords(V1=list(series_map.keys()))
    return out.transpose("S","D","E","V1")
