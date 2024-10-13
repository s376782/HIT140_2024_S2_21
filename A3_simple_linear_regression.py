import pandas as pd
import pathlib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

from A3_datawrangling import *

for wellbeing_field in wellbeing_fields:
    print('======', wellbeing_field, '======')

    df = getDataFrame(wellbeing_field)[['total-time', wellbeing_field]]

    # Separate explanatory variables (x) from the response variable (y)
    X = df.iloc[:,:-1].values
    y = df.iloc[:,-1].values

    # Split dataset into 60% training and 40% test sets 
    # Note: other % split can be used.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

    # Build a linear regression model
    model = LinearRegression()

    # Train (fit) the linear regression model using the training set
    model.fit(X_train, y_train)

    # Print the intercept and coefficient learned by the linear regression model
    # print("Intercept: ", model.intercept_)
    # print("Coefficient: ", model.coef_)

    # Use linear regression to predict the values of (y) in the test set
    # based on the values of x in the test set
    y_pred = model.predict(X_test)

    # Optional: Show the predicted values of (y) next to the actual values of (y)
    df_pred = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
    # print(df_pred)

    # Compute standard performance metrics of the linear regression:

    # Mean Absolute Error
    mae = metrics.mean_absolute_error(y_test, y_pred)
    # Mean Squared Error
    mse =  metrics.mean_squared_error(y_test, y_pred)
    # Root Mean Square Error
    rmse = metrics.root_mean_squared_error(y_test, y_pred)
    # Normalised Root Mean Square Error
    y_max = y.max()
    y_min = y.min()
    rmse_norm = rmse / (y_max - y_min)

    # R-Squared
    r_2 = metrics.r2_score(y_test, y_pred)

    print("MLP performance:")
    print("MAE: ", mae)
    print("MSE: ", mse)
    print("RMSE: ", rmse)
    print("RMSE (Normalised): ", rmse_norm)
    print("R^2: ", r_2)

    print(f'{wellbeing_field} = {model.intercept_:.4f}' +
          f'{" + " if model.coef_[0] >= 0 else " - "} {abs(model.coef_[0]):.4f}(Total Screen Time)')
    
    plt.scatter(df['total-time'], df[wellbeing_field])
    plt.xlabel("Total screen time")
    plt.ylabel(wellbeing_field)
    pathlib.Path('output/simple_linear_regression').mkdir(parents=True, exist_ok=True) 
    plt.savefig(f'output/simple_linear_regression/{wellbeing_field}.png')
    plt.clf()
