# Import Python library
import pandas as pd
import numpy as np

# Read 3 datasets and set index for ID in each dataset
df1 = pd.read_csv('data/dataset1.csv').set_index(['ID'])
df2 = pd.read_csv('data/dataset2.csv').set_index(['ID'])
df3 = pd.read_csv('data/dataset3.csv').set_index(['ID'])

# Insert all variable names of well-being into an array
wellbeing_fields = ['Optm','Usef','Relx','Intp','Engs','Dealpr','Thcklr','Goodme','Clsep','Conf','Mkmind','Loved','Intthg','Cheer']

# Compute total screening time per week
df2['total_we'] = df2['C_we']*5 + df2['G_we']*5 + df2['S_we']*5 + df2['T_we']*5
df2['total_wk'] = df2['C_wk']*2 + df2['G_wk']*2 + df2['S_wk']*2 + df2['T_wk']*2
df2['total'] = df2['total_we'] + df2['total_wk']

# Compute total well being score
df3['wellbeing-score'] = df3[wellbeing_fields].sum(axis=1)

# Create new dataframe for all data by joining 3 datasets
df = df3.join(df2, how='inner').join(df1, how='inner')

# Compute quartile1(25%) and quartile3(75%) for total screening time per week
total_q1, total_q3 = np.percentile(df['total'].to_numpy(), [25, 75])

# Compute IQR and fence to indentify outliers
total_iqr = total_q3 - total_q1 #Compute IQR
lower_fence = total_q1 - (1.5*total_iqr) #Compute lower_fence
higher_fence = total_q3 + (1.5*total_iqr) #Compute higher_fence

# Screening time group
# Low screening time group: include all people have total screening time per week lower than value of lower fence
df_low_st = df.loc[df['total'] < total_q1].loc[df['total'] > lower_fence]
# High screening time group: include all people have total screening time per week higher than value of higher fence
df_high_st = df.loc[df['total'] > total_q3].loc[df['total'] < higher_fence]

# Create new dataframe follow condition of groups
# Gender groups
df_g0 = df.loc[df['gender'] == 0] #group for otherwise gender
df_g1 = df.loc[df['gender'] == 1] #group for male
df_g0_wo_outliers = df_g0.loc[df_g0['total'] > lower_fence].loc[df_g0['total'] < higher_fence]
df_g1_wo_outliers = df_g1.loc[df_g1['total'] > lower_fence].loc[df_g1['total'] < higher_fence]

# Minority group
df_m0 = df.loc[df['minority'] == 0] #group for the majority ethnic group of the country
df_m1 = df.loc[df['minority'] == 1] #group for otherwise minority group
df_m0_wo_outliers = df_m0.loc[df_m0['total'] > lower_fence].loc[df_m0['total'] < higher_fence]
df_m1_wo_outliers = df_m1.loc[df_m1['total'] > lower_fence].loc[df_m1['total'] < higher_fence]

# Deprivation group
df_d1 = df.loc[df['deprived'] == 1] #group with high deprivation indices with high scores on unemployment, crime, poor public services, and barriers to housing
df_d0 = df.loc[df['deprived'] == 0] #group for otherwise
df_d0_wo_outliers = df_d0.loc[df_d0['total'] > lower_fence].loc[df_d0['total'] < higher_fence]
df_d1_wo_outliers = df_d1.loc[df_d1['total'] > lower_fence].loc[df_d1['total'] < higher_fence]
