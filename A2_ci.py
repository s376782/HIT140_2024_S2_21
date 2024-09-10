from A2_datawrangling import *

def calculate_ci(col: pd.Series, confidence: float = 0.95):
    import statsmodels.stats.weightstats as stm
    # import math
    # x_bar = col.mean();
    # s = col.std()
    # n = col.shape[0]

    # std_err = s / math.sqrt(n)

    # # confidence level, significance level, and degrees of freedom
    sig_lvl = 1 - confidence
    # df = n - 1

    # return stm._zconfint_generic(x_bar, std_err, df, sig_lvl, "two-sided")
    ds = stm.DescrStatsW(col.values)
    return ds.tconfint_mean(sig_lvl)

dfs = {
    'df_high_st': df_high_st,
    'df_low_st': df_low_st,
    'df_g1': df_g1,
    'df_g0': df_g0,
    'df_d1': df_d1,
    'df_d0': df_d0,
    'df_m1': df_m1,
    'df_m0': df_m0
}

fields = wellbeing_fields + ['total']

for name, d in dfs.items():
    print(f'==================================================')
    for field in fields:
        low, high = calculate_ci(d[field])
        print(f'Dataframe `{name}` field `{field}`: {low:.3f} - {high:.3f}')
