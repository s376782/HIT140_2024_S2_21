import statsmodels.api as sm
from pandas import DataFrame
from sklearn.preprocessing import StandardScaler, PowerTransformer

from A3_datawrangling import *

def linearRegression(df: DataFrame, fit_transform = False, zscore_standardisation = False):
    # Separate explanatory variables (X) from the response variable (y)
    X = df.iloc[:,:-1]
    y = df.iloc[:,-1]

    if fit_transform:
        scaler = StandardScaler()
        X_std = scaler.fit_transform(X.values)
        X = pd.DataFrame(X_std, index=X.index, columns=X.columns)
        X = sm.add_constant(X)

    if zscore_standardisation:
        scaler = PowerTransformer()
        X_pow = scaler.fit_transform(X.values)
        X = pd.DataFrame(X_pow, index=X.index, columns=X.columns)

    # build the linear regression using statsmodels
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    print(model.summary())

for wellbeing_field in wellbeing_fields:
    df = getDataFrame(wellbeing_field, False)

    linearRegression(df)

    # Optimisation #1: Non-linear transformation
    # inspect the linearity between each explanatory variable and the response variable in the dataset
    # => No linear relationship between the two variables was found.

    # Optimisation #2: Remove multicollinearity
    linearRegression(df.drop(['C_we'], axis=1))
    linearRegression(df.drop(['C_wk'], axis=1))
    linearRegression(df.drop(['S_we'], axis=1))
    linearRegression(df.drop(['S_wk'], axis=1))
    linearRegression(df.drop(['T_we'], axis=1))
    linearRegression(df.drop(['T_wk'], axis=1))

    # Optimisation #3: Rescale the explanatory variables
    linearRegression(df, fit_transform=True)

    # Optimisation #4: Gaussian transformation
    linearRegression(df, zscore_standardisation=True)
