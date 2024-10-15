#code to run this file to save all result into an excel file:python A3_ordinal_linear_regression.py > result.txt
import numpy as np
from statsmodels.miscmodels.ordinal_model import OrderedModel
from sklearn.model_selection import train_test_split

from A3_datawrangling import *

for wellbeing_field in wellbeing_fields:
    print('======', wellbeing_field, '======')

    df = getDataFrame(wellbeing_field, True)

    # Separate explanatory variables (x) from the response variable (y)
    X = df.iloc[:,:-1]
    y = df.iloc[:,-1]

    # Split dataset into 60% training and 40% test sets 
    # Note: other % split can be used.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
    
    # Define the ordinal regression model using the probit distribution
    model = OrderedModel(y_train, X_train, distr='logit')
    
    # Fit the model with model, refers to the Broyden-Fletcher-Goldfarb-Shanno algorithm
    result = model.fit(method='bfgs')

    # Predict probabilities for each category
    y_pred_prob = result.model.predict(result.params, exog=X_test)
    
    # Show the summary of the model
    print(result.summary())
 
 
    # Pearson Chi-Square Test
    # Predict probabilities for each category
    y_pred_prob = result.model.predict(result.params, exog=X_test)
    # Convert predicted probabilities to the most likely category
    y_pred = np.argmax(y_pred_prob, axis=1)
    pearson_chi2 = np.sum((y_test - y_pred) ** 2 / y_pred)
    print(f"Pearson Chi-Square: {pearson_chi2}")


    # McFadden's Pseudo R-squared
    LL_full = result.llf
    LL_null = result.llnull
    pseudo_r2 = 1 - (LL_full / LL_null)
    print(f"McFadden's Pseudo R-squared: {pseudo_r2}")
