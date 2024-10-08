# Import Python library
import pandas as pd

# Read 3 datasets and set index for ID in each dataset
df1 = pd.read_csv('data/dataset1.csv').set_index(['ID'])
df2 = pd.read_csv('data/dataset2.csv').set_index(['ID'])
df3 = pd.read_csv('data/dataset3.csv').set_index(['ID'])

# Insert all variable names of well-being into an array
wellbeing_fields = df3.columns.values

def getDataFrame(wellbeing_field, total = True):
    global df1, df2, df3

    if total:
        # Compute total screening time per week
        df2['total'] = df2['C_we']*5 + df2['G_we']*5 + df2['S_we']*5 + df2['T_we']*5 + df2['C_wk']*2 + df2['G_wk']*2 + df2['S_wk']*2 + df2['T_wk']*2

        # Remove invalid data
        df2 = df2.loc[df2['total'] <= 168]

    # Compute total well being score
    #df3['wellbeing-score'] = df3[wellbeing_fields].sum(axis=1)

    # Create new dataframe for all data by joining 3 datasets
    return df1.join(df2, how='inner').join(df3[[wellbeing_field]], how='inner')
