# ttest to figure out relationship between gender and screening time
# Import clean data from A2 file
from A2 import *

# Function to remove outliers using IQR
def remove_outliers(df, field):
    Q1 = df[field].quantile(0.25)
    Q3 = df[field].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[field] >= lower_bound) & (df[field] <= upper_bound)]


# Define t-test function
def ttest(df1, df2, field, equal_var=False, alternative="two-sided"):
    import scipy.stats as st
    
    sample1 = df1[field].to_numpy()
    sample2 = df2[field].to_numpy()

    # the basic statistics of sample 1:
    x_bar1 = st.tmean(sample1)
    s1 = st.tstd(sample1)
    n1 = len(sample1)

    # the basic statistics of sample 2:
    x_bar2 = st.tmean(sample2)
    s2 = st.tstd(sample2)
    n2 = len(sample2)

    # perform two-sample t-test
    # null hypothesis: mean of sample 1 = mean of sample 2
    # alternative hypothesis: mean of sample 1 is greater than mean of sample 2 (one-sided test)
    # note the argument equal_var=False, which assumes that two populations do not have equal variance
    t_stats, p_val = st.ttest_ind_from_stats(
        x_bar1, s1, n1,
        x_bar2, s2, n2,
        equal_var, alternative
    )
    return t_stats, p_val

dfs = {
    'df_high_st <> df_low_st': (df_high_st, df_low_st),
    'df_g1 <> df_g0': (df_g1, df_g0),
    'df_d1 <> df_d0': (df_d1, df_d0),
    'df_m1 <> df_m0': (df_m1, df_m0)
}
for name, d in dfs.items():
    print(f'==================================================')
    for field in wellbeing_fields:
        t_stat, p_val = ttest(d[0], d[1], field)
        #print(f'`{name}` field `{field}`: Stats: {t_stat:.3f}, PValue: {p_val:.3f}')
        if (p_val < 0.005):
            print(f'`{name}` field `{field}`: {p_val:.4f} Y')
        else:
            print(f'`{name}` field `{field}`: {p_val:.4f} N')

