# Import Python library
import pandas as pd

# Remove outlier
def remove_outliers(df):
    for variable in df.columns.values:
        # Filter out the outliers
        Q1 = df[variable].quantile(0.25)
        Q3 = df[variable].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[df[variable] >= lower_bound][df[variable] <= upper_bound]
    return df

# Read 3 datasets and set index for ID in each dataset
df1 = pd.read_csv('data/dataset1.csv').set_index(['ID'])
df2 = pd.read_csv('data/dataset2.csv').set_index(['ID'])
df3 = pd.read_csv('data/dataset3.csv').set_index(['ID'])

# Insert all variable names of well-being and screening time into an array
wellbeing_fields = df3.columns.values

# Compute total well being score
df3['total-score'] = df3[df3.columns.values].sum(axis=1)

wellbeing_fields_with_total = df3.columns.values

# print(wellbeing_fields)
# print(wellbeing_fields_with_total)

# Compute total screening time per week
df2Total = pd.DataFrame(columns=['total-time'])
df2Total['total-time'] = df2['C_we']*5 + df2['G_we']*5 + df2['S_we']*5 + df2['T_we']*5 + df2['C_wk']*2 + df2['G_wk']*2 + df2['S_wk']*2 + df2['T_wk']*2

# Remove invalid data
df2Total = df2Total.loc[df2Total['total-time'] <= 168]

# Remove outlier in dataset2
df2 = remove_outliers(df2)
df2Total = remove_outliers(df2Total)

# print(df2.info())
# print(df2Total.info())
# print(df2.head())
# print(df2Total.head())

def getDataFrame(wellbeing_field, include_dataset1 = False, include_total_time = False):
    global df1, df2, df3

    df = df2
    if include_dataset1:
        df = df1.join(df, how='inner')
    if include_total_time:
        df = df.join(df2Total, how='inner')

    # Create new dataframe for all data by joining 2 datasets
    df = df.join(df3[[wellbeing_field]], how='inner')
    
    return df
