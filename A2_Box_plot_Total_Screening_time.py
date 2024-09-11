import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from A2_datawrangling import *


#extract the values from the column Total_time_on_screen into a numpy array
sample = df['total'].to_numpy()
#print(sample)

df1 = pd.DataFrame(df['total'])

# print summary statistics of the "Total_time_spend_on_screen" 
print(df['total'].describe())

# Key statistics
median = np.median(sample)
q1 = np.percentile(df1, 25)
q3 = np.percentile(df1, 75)
min_val = np.min(sample)
max_val = np.max(sample)

#print(median, q1, q3, min_val, max_val)

# Box plot
sns.boxplot(df1)    # Create a boxplot using seaborn

# Display the labels
plt.text(1.05, median, f'Median: {median:.2f}', ha='left', va='center', color='blue')
plt.text(1.05, q1, f'Q1: {q1:.2f}', ha='left', va='center', color='blue')
plt.text(1.05, q3, f'Q3: {q3:.2f}', ha='left', va='center', color='blue')
plt.text(1.05, min_val, f'Min: {min_val:.2f}', ha='left', va='center', color='blue')
plt.text(1.05, max_val, f'Max: {max_val:.2f}', ha='left', va='center', color='blue')


plt.title("Boxplot of Total screening time Data")    # Add a title
plt.show()       # Show the plot

df_outliers = df.loc[df['total'] >= higher_fence]

print(df_outliers['total'].to_numpy())





