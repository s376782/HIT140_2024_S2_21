import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from A3_datawrangling import *


def linear_regression_analysis(wellbeing_fields, group_column, group_value):
    for wellbeing_field in wellbeing_fields:
        df = getDataFrame(wellbeing_field, True, True)

        print('======', group_column, group_value, wellbeing_field, '======')
        
        df = df[df[group_column] == group_value]

        # Select relevant columns
        df = df[['total-time', wellbeing_field]]

        # Separate explanatory variables (X) from the response variable (y)
        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values

        # Split dataset into 60% training and 40% test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

        # Build and train a linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Use the model to predict values in the test set
        y_pred = model.predict(X_test)

        # Compute standard performance metrics
        mae = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        rmse = metrics.root_mean_squared_error(y_test, y_pred)  # RMSE
        y_max = y.max()
        y_min = y.min()
        rmse_norm = rmse / (y_max - y_min)  # Normalized RMSE
        r_2 = metrics.r2_score(y_test, y_pred)

        # Output performance metrics
        print("MLP performance:")
        print("MAE: ", mae)
        print("MSE: ", mse)
        print("RMSE: ", rmse)
        print("RMSE (Normalised): ", rmse_norm)
        print("R^2: ", r_2)

        # Output regression equation
        print(f'{wellbeing_field} = {model.intercept_:.4f}' +
              f'{" + " if model.coef_[0] >= 0 else " - "} {abs(model.coef_[0]):.4f}(Total Screen Time)')

        # Create scatter plot
        plt.scatter(df['total-time'], df[wellbeing_field])
        plt.xlabel("Total screen time")
        plt.ylabel(wellbeing_field)
        plt.title(f'{wellbeing_field} VS Total screening time ({group_column} = {group_value})')
        # Create output directory and save plot
        output_directory = pathlib.Path(f'output/simple_linear_regression/{group_column}{group_value}')
        output_directory.mkdir(parents=True, exist_ok=True)  
        plt.savefig(output_directory / f'{wellbeing_field}.png')
        plt.clf()  # Clear the current figure


# Define group settings for analysis
groups = [
    ('minority', 0),
    ('minority', 1),
    ('gender', 0),
    ('gender', 1),
    ('deprived', 0),
    ('deprived', 1)
]

# Loop through groups and perform regression analysis
for group_column, group_value in groups:
    linear_regression_analysis(wellbeing_fields_with_total, group_column, group_value)
