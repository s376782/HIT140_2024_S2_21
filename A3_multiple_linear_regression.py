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

# ============ Optm =============
df = getDataFrame('Optm', False)

linearRegression(df)

# try to remove the C_we variable
# linearRegression(df.drop(['C_we'], axis=1))
# linearRegression(df.drop(['C_wk'], axis=1))
# linearRegression(df.drop(['S_we'], axis=1))
# linearRegression(df.drop(['S_wk'], axis=1))
# linearRegression(df.drop(['T_we'], axis=1))
# linearRegression(df.drop(['T_wk'], axis=1))

linearRegression(df, fit_transform=True)
linearRegression(df, zscore_standardisation=True)

# for wellbeing_field in wellbeing_fields:
#     print('======', wellbeing_field, '======')

#     df = getDataFrame(wellbeing_field, False)

#     # Separate explanatory variables (x) from the response variable (y)
#     X = df.iloc[:,:-1]
#     y = df.iloc[:,-1]

#     # build the linear regression using statsmodels
#     X = sm.add_constant(X)
#     model = sm.OLS(y, X).fit()
#     print(model.summary())

    # # Split dataset into 60% training and 40% test sets 
    # # Note: other % split can be used.
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

    # # Build a linear regression model
    # model = LinearRegression()

    # # Train (fit) the linear regression model using the training set
    # model.fit(X_train, y_train)


    # # Print the intercept and coefficient learned by the linear regression model
    # # print("Intercept: ", model.intercept_)
    # # print("Coefficient: ", model.coef_)

    # # Use linear regression to predict the values of (y) in the test set
    # # based on the values of x in the test set
    # y_pred = model.predict(X_test)

    # # Optional: Show the predicted values of (y) next to the actual values of (y)
    # df_pred = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
    # # print(df_pred)

    # # Compute standard performance metrics of the linear regression:

    # # Mean Absolute Error
    # mae = metrics.mean_absolute_error(y_test, y_pred)
    # # Mean Squared Error
    # mse = metrics.mean_squared_error(y_test, y_pred)
    # # Root Mean Square Error
    # rmse =  metrics.root_mean_squared_error(y_test, y_pred)
    # # Normalised Root Mean Square Error
    # y_max = y.max()
    # y_min = y.min()
    # rmse_norm = rmse / (y_max - y_min)

    # # R-Squared
    # r_2 = metrics.r2_score(y_test, y_pred)

    # print("MLP performance:")
    # print("MAE: ", mae)
    # print("MSE: ", mse)
    # print("RMSE: ", rmse)
    # print("RMSE (Normalised): ", rmse_norm)
    # print("R^2: ", r_2)

    # print(f'{wellbeing_field} = {model.intercept_:.4f}', end='')
    # for i, name in enumerate(df.iloc[:,:-1].columns.values):
    #     value = model.coef_[i]
    #     sign = ' + ' if value > 0 else ' - '
    #     print(f'{sign}{abs(value):.4f}({name})', end='')
    # print()
