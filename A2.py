import pandas as pd
import numpy as np

wellbeing_fields = ['Optm','Usef','Relx','Intp','Engs','Dealpr','Thcklr','Goodme','Clsep','Conf','Mkmind','Loved','Intthg','Cheer']

df1 = pd.read_csv('data/dataset1.csv').set_index(['ID'])
df2 = pd.read_csv('data/dataset2.csv').set_index(['ID'])
df3 = pd.read_csv('data/dataset3.csv').set_index(['ID'])

df2['total_we'] = df2['C_we']*5 + df2['G_we']*5 + df2['S_we']*5 + df2['T_we']*5
df2['total_wk'] = df2['C_wk']*2 + df2['G_wk']*2 + df2['S_wk']*2 + df2['T_wk']*2
df2['total'] = df2['total_we'] + df2['total_wk']

df3['wellbeing-score'] = df3[wellbeing_fields].sum(axis=1)

df = df3.join(df2, how='inner').join(df1, how='inner')

df_g0 = df.loc[df['gender'] == 0]
df_g1 = df.loc[df['gender'] == 1]
df_m0 = df.loc[df['minority'] == 0]
df_m1 = df.loc[df['minority'] == 1]
df_d0 = df.loc[df['deprived'] == 0]
df_d1 = df.loc[df['deprived'] == 1]

total_q1, total_q3 = np.percentile(df['total'].to_numpy(), [25, 75])
total_iqr = total_q3 - total_q1
lower_fence = total_q1 - (1.5*total_iqr)
higher_fence = total_q3 + (1.5*total_iqr)
df_low_st = df.loc[df['total'] < total_q1].loc[df['total'] > lower_fence]
df_high_st = df.loc[df['total'] > total_q3].loc[df['total'] < higher_fence]

# df_g0_m0 = df.loc[df['gender'] == 0].loc[df['minority'] == 0]
# df_g0_m1 = df.loc[df['gender'] == 0].loc[df['minority'] == 1]
# df_g0_d0 = df.loc[df['gender'] == 0].loc[df['deprived'] == 0]
# df_g0_d1 = df.loc[df['gender'] == 0].loc[df['deprived'] == 1]
# df_g1_m0 = df.loc[df['gender'] == 1].loc[df['minority'] == 0]
# df_g1_m1 = df.loc[df['gender'] == 1].loc[df['minority'] == 1]
# df_g1_d0 = df.loc[df['gender'] == 1].loc[df['deprived'] == 0]
# df_g1_d1 = df.loc[df['gender'] == 1].loc[df['deprived'] == 1]
# df_m0_d0 = df.loc[df['minority'] == 0].loc[df['deprived'] == 0]
# df_m0_d1 = df.loc[df['minority'] == 0].loc[df['deprived'] == 1]

# df_g0_m0_d0 = df.loc[df['gender'] == 0].loc[df['minority'] == 0].loc[df['deprived'] == 0]
# df_g0_m0_d1 = df.loc[df['gender'] == 0].loc[df['minority'] == 0].loc[df['deprived'] == 1]
# df_g0_m1_d0 = df.loc[df['gender'] == 0].loc[df['minority'] == 1].loc[df['deprived'] == 0]
# df_g0_m1_d1 = df.loc[df['gender'] == 0].loc[df['minority'] == 1].loc[df['deprived'] == 1]
# df_g1_m0_d0 = df.loc[df['gender'] == 1].loc[df['minority'] == 0].loc[df['deprived'] == 0]
# df_g1_m0_d1 = df.loc[df['gender'] == 1].loc[df['minority'] == 0].loc[df['deprived'] == 1]
# df_g1_m1_d0 = df.loc[df['gender'] == 1].loc[df['minority'] == 1].loc[df['deprived'] == 0]
# df_g1_m1_d1 = df.loc[df['gender'] == 1].loc[df['minority'] == 1].loc[df['deprived'] == 1]
