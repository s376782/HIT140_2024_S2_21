# Import clean data from A2 file
from A2_datawrangling import *

def utest(df1, df2, field, use_continuity=True, alternative='two-sided'):
    import scipy.stats as st

    sample1 = df1[field].to_numpy()
    sample2 = df2[field].to_numpy()

    # perform two-sample Mann-Whitney U test
    u_stats, p_val = st.mannwhitneyu(
        sample1, sample2,
        use_continuity, alternative
    )

    return u_stats, p_val

dfs = {
    'df_high_st & df_low_st': (df_high_st, df_low_st),
    'df_g1 & df_g0': (df_g1_wo_outliers, df_g0_wo_outliers),
    'df_d1 & df_d0': (df_d1_wo_outliers, df_d0_wo_outliers),
    'df_m1 & df_m0': (df_m1_wo_outliers, df_m0_wo_outliers)
}

for alternative in ['two-sided', 'less', 'greater']:
    for name, d in dfs.items():
        print(f'==================================================')
        for field in wellbeing_fields:
            u_stats, p_val = utest(d[0], d[1], field, alternative=alternative)
            print(f'({alternative}) Mann-Whitney U test for `{name}` - field `{field}`: Stats: {u_stats:.4f}, PValue: {p_val:.4f}')
    