import pandas as pd
import matplotlib.pyplot as plt
from A2_datawrangling import *

# Total Screening Time by (Gender, Minority, Deprived)
print(df_g0 ['total'].describe())
print(df_g1 ['total'].describe())
print(df_m0 ['total'].describe())
print(df_m1 ['total'].describe())
print(df_d0 ['total'].describe())
print(df_d1 ['total'].describe())


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

statistics(df_g1 ['total'], 'orange', 'black', 
           "Histogram of Total time on screen by gender (Male)",
           "Time (in hours)", "Number of adolescent", 5)
statistics(df_g0 ['total'], 'pink', 'black', 
           "Histogram of Total time on screen by gender (Otherwise)",
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

