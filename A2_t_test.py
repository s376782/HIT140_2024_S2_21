# import library
import pandas as pd
import numpy as np
import scipy.stats as st
# Import clean data from A2 file
from A2_datawrangling import *


#Define t-test function
def ttest(df1, df2, fields , equal_var=False, alternative="two-sided"):
    t_stats_list = []
    p_val_list = []
    for field in fields:
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
    # alternative hypothesis: mean of sample 1 is different with mean of sample 2 (two-sided test)
    # note the argument equal_var=False, which assumes that two populations do not have equal variance
        t_stats, p_val = st.ttest_ind_from_stats(
            x_bar1, s1, n1,
            x_bar2, s2, n2,
            equal_var=equal_var, alternative=alternative
        )   
        t_stats_list.append(t_stats)
        p_val_list.append(p_val)
    print("t-stats list:", [f"{t_stat:.4f}" for t_stat in t_stats_list])
    print("p-value list:", [f"{p_val:.4f}" for p_val in p_val_list])
    return t_stats_list, p_val_list

# RUN t - TEST 
# t-test for gender and screening time
_,p_val = ttest(df_g0, df_g1, fields = ['total'])


# t-test for gender and wellbeing fields
_,p_val = ttest(df_g0, df_g1,fields = wellbeing_fields)


# t-test for deprived and screening time
_,p_val = ttest(df_d0, df_d1, fields = ['total'])


# t-test for deprived and wellbeing fields
_,p_val = ttest(df_d0, df_d1, fields = wellbeing_fields)


# t-test for minority and each wellbeing fields
_,p_val = ttest(df_m0, df_m1,fields = ['total'])


# t-test for minority and each wellbeing fields
_,p_val = ttest(df_m0, df_m1,fields = wellbeing_fields)


# t-test for screening time and wellbeing fields
_,p_val = ttest(df_low_st,df_high_st , fields = wellbeing_fields)
    
