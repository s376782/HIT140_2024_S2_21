import statsmodels.api as sm
from pandas import DataFrame
import numpy as np
from A3_datawrangling import *

def Nontransformation(df, df2: DataFrame, Log=False, Exponential=False, Quadratic=False, Reciprocal=False):
    # Collect all collumn name of df2
    variable_fields = df2.columns.values
    for variable in variable_fields:
        if Exponential:
            df[variable+'TRANS'] = df[variable].apply(np.exp)
            df.insert(0, variable+'TRANS', df.pop(variable+'TRANS'))
        elif Quadratic:
            df[variable+'TRANS'] = df[variable].apply(lambda x: x**2)
            df.insert(0, variable+'TRANS', df.pop(variable+'TRANS'))
        elif Reciprocal:
            df[variable+'TRANS'] = df[variable].apply(lambda x: 1/x if x != 0 else np.nan)
            df.insert(0, variable +'TRANS', df.pop(variable +'TRANS'))

    # Drop variable before transforming
        df = df.drop(variable, axis=1) 
    
        # Separate explanatory variables (X) from the response variable (y)
    X = df.iloc[:, :-1] 
    y = df.iloc[:, -1]   
    X = sm.add_constant(X)  
    model = sm.OLS(y, X).fit()  
    print(model.summary())  

# Call Nontransformation for each wellbeing_field
for wellbeing_field in wellbeing_fields:
    df = getDataFrame(wellbeing_field, True)
    
    # Exponential
    # print(f"\nExponential Transformation for {wellbeing_field}")
    # Nontransformation(df, df2, Exponential=True)
    
    # Quadratic
    print(f"\nQuadratic Transformation for {wellbeing_field}")
    Nontransformation(df, df2, Quadratic=True)
    
    # # Reciprocals
    # print(f"\nReciprocal Transformation for {wellbeing_field}")
    # Nontransformation(df, df2,Reciprocal=True)
