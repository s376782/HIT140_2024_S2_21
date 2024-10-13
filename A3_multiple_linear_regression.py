import numpy as np
import statsmodels.api as sm
from pandas import DataFrame
from sklearn.preprocessing import StandardScaler, PowerTransformer

from A3_datawrangling import *

def linearRegression(df: DataFrame, prefix = 'Normal', fit_transform = False, zscore_standardisation = False, detail = False):
    # Separate explanatory variables (X) from the response variable (y)
    X = df.iloc[:,:-1]
    y = df.iloc[:,-1]

    if fit_transform:
        scaler = StandardScaler()
        X_std = scaler.fit_transform(X.values)
        X = pd.DataFrame(X_std, index=X.index, columns=X.columns)

    if zscore_standardisation:
        scaler = PowerTransformer()
        X_pow = scaler.fit_transform(X.values)
        X = pd.DataFrame(X_pow, index=X.index, columns=X.columns)

    # build the linear regression using statsmodels
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    if detail:
        print(prefix, y.name)
        print(model.summary())
    else:
        print(prefix, y.name, model.rsquared, model.rsquared_adj)

for wellbeing_field in wellbeing_fields_with_total:
    df = getDataFrame(wellbeing_field, False)
    linearRegression(df, detail=True)

for wellbeing_field in wellbeing_fields_with_total:
    df = getDataFrame(wellbeing_field, True)
    linearRegression(df, detail=True)

for wellbeing_field in wellbeing_fields_with_total:
    df = getDataFrame(wellbeing_field, True)

    # Optimisation #1: Non-linear transformation
    for variable in df.iloc[:,:-1].columns.values:
        # Log
        df_c = df.copy()
        df_c[variable] = df_c[variable].apply(lambda x: np.log(x) if x != 0 else 0)
        linearRegression(df_c, 'Non-linear transformation (Log)')

        # Exponential
        df_c = df.copy()
        df_c[variable] = df_c[variable].apply(np.exp)
        linearRegression(df_c, 'Non-linear transformation (Exponential)')

        # Quandratic
        df_c = df.copy()
        df_c[variable] = df_c[variable].apply(lambda x: x**2)
        linearRegression(df_c, 'Non-linear transformation (Quandratic)')

        # Reciprocal
        df_c = df.copy()
        df_c[variable] = df_c[variable].apply(lambda x: 1/x if x != 0 else 0)
        linearRegression(df_c, 'Non-linear transformation (Reciprocal)')

    # Optimisation #2: Remove multicollinearity
    linearRegression(df.drop(['C_we'], axis=1), 'Remove multicollinearity (C_we)')
    linearRegression(df.drop(['C_wk'], axis=1), 'Remove multicollinearity (C_wk)')
    linearRegression(df.drop(['S_we'], axis=1), 'Remove multicollinearity (S_we)')
    linearRegression(df.drop(['S_wk'], axis=1), 'Remove multicollinearity (S_wk)')
    linearRegression(df.drop(['T_we'], axis=1), 'Remove multicollinearity (T_we)')
    linearRegression(df.drop(['T_wk'], axis=1), 'Remove multicollinearity (T_wk)')

    # Optimisation #3: Rescale the explanatory variables
    linearRegression(df, 'Rescale the explanatory variables', fit_transform=True)

    # Optimisation #4: Gaussian transformation
    linearRegression(df, 'Gaussian transformation', zscore_standardisation=True)
