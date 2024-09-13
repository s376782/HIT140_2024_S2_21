import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew
from A2_datawrangling import *

# Total Screening Time by (Gender, Minority, Deprived)
print(df_g0 ['total'].describe())
print(df_g1 ['total'].describe())
print(df_m0 ['total'].describe())
print(df_m1 ['total'].describe())
print(df_d0 ['total'].describe())
print(df_d1 ['total'].describe())

# Mode
print('Mode_g0', df_g0 ['total'].mode()[0])
print('Mode_g1', df_g1 ['total'].mode()[0])
print('Mode_m0', df_m0 ['total'].mode()[0])
print('Mode_m1', df_m1 ['total'].mode()[0])
print('Mode_d0', df_d0 ['total'].mode()[0])
print('Mode_d1', df_d1 ['total'].mode()[0])

# Skewness
print('Skewness_g0', skew(df_g0['total']))
print('Skewness_g1', skew(df_g1['total']))
print('Skewness_m0', skew(df_m0['total']))
print('Skewness_m1', skew(df_m1['total']))
print('Skewness_d0', skew(df_d0['total']))
print('Skewness_d1', skew(df_d1['total']))


# Compute lower and higher fences specifically
lower_fence_g0, higher_fence_g0 = compute_fences(df_g0['total'].to_numpy())
lower_fence_g1, higher_fence_g1 = compute_fences(df_g1['total'].to_numpy())
lower_fence_d0, higher_fence_d0 = compute_fences(df_d0['total'].to_numpy())
lower_fence_d1, higher_fence_d1 = compute_fences(df_d1['total'].to_numpy())
lower_fence_m0, higher_fence_m0 = compute_fences(df_m0['total'].to_numpy())
lower_fence_m1, higher_fence_m1 = compute_fences(df_m1['total'].to_numpy())

# Print the outliers
print("lower_fence_g0: ", lower_fence_g0)
print("higher_fence_g0: ", higher_fence_g0)
print("lower_fence_g1: ", lower_fence_g1)
print("higher_fence_g1: ", higher_fence_g1)

print("lower_fence_d0: ", lower_fence_d0)
print("higher_fence_d0: ", higher_fence_d0)
print("lower_fence_d1: ", lower_fence_d1)
print("higher_fence_d1: ", higher_fence_d1)

print("lower_fence_m0: ", lower_fence_m0)
print("higher_fence_m0: ", higher_fence_m0)
print("lower_fence_m1: ", lower_fence_m1)
print("higher_fence_m1: ", higher_fence_m1)

# Outliers
df_outliers_g0 = df_g0.loc[df_g0['total'] >= higher_fence_g0]
df_outliers_g1 = df_g1.loc[df_g1['total'] >= higher_fence_g1]
df_outliers_d0 = df_d0.loc[df_d0['total'] >= higher_fence_d0]
df_outliers_d1 = df_d1.loc[df_d1['total'] >= higher_fence_d1]
df_outliers_m0 = df_m0.loc[df_m0['total'] >= higher_fence_m0]
df_outliers_m1 = df_m1.loc[df_m1['total'] >= higher_fence_m1]

print("Outliers: Gender = Otherwise", df_outliers_g0['total'].to_numpy())
print("Outliers: Gender = Male", df_outliers_g1['total'].to_numpy())
print("Outliers: Deprivation = Otherwise", df_outliers_d0['total'].to_numpy())
print("Outliers: Deprivation = Deprived", df_outliers_d1['total'].to_numpy())
print("Outliers: Ethnic group = Majority", df_outliers_m0['total'].to_numpy())
print("Outliers: Ethnic group = Otherwise", df_outliers_m1['total'].to_numpy())


def statistics(col: pd.Series, color, edgecolor, title, xlabel, ylabel, bin_width):
    sample = col.to_numpy()

    # get bin width of 5 hours
    max_val = sample.max()
    min_val = sample.min()
    the_range = max_val - min_val
    #bin_width = 5
    bin_count= int(the_range/bin_width)

    # plot histogram of Total time on screen distribution
    plt.hist(sample, color=color, edgecolor=edgecolor, bins=bin_count)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


statistics(df_g0 ['total'], 'pink', 'black', 
           "Histogram of Total time on screen by gender (Otherwise)",
           "Time (in hours)", "Number of adolescent", 5)
statistics(df_g1 ['total'], 'orange', 'black', 
           "Histogram of Total time on screen by gender (Male)",
           "Time (in hours)", "Number of adolescent", 5)

statistics(df_m0 ['total'], 'green', 'black', 
           "Histogram of Total time on screen by ethnic group (Majority)",
           "Time (in hours)", "Number of adolescent", 5)
statistics(df_m1 ['total'], 'yellow', 'black', 
           "Histogram of Total time on screen by ethnic group (Otherwise)",
           "Time (in hours)", "Number of adolescent", 5)

statistics(df_d0 ['total'], 'darkblue', 'black', 
           "Histogram of Total time on screen by deprivation (Deprived)",
           "Time (in hours)", "Number of adolescent", 5)
statistics(df_d1 ['total'], 'gray', 'black', 
           "Histogram of Total time on screen by deprivation (Otherwise)",
           "Time (in hours)", "Number of adolescent", 5)




