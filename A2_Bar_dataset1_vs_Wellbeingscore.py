import matplotlib.pyplot as plt
import numpy as np
from A2_datawrangling import *

def bar_chart(df1, df2, title, label1, label2):
    for field in wellbeing_fields:

        # Data for the chart
        scores = [1, 2, 3, 4, 5]
        value1 = [df1.loc[df1[field] == i].shape[0] for i in scores]
        value2 = [df2.loc[df2[field] == i].shape[0] for i in scores]

        # Setting the positions and width for the bars
        bar_width = 0.35
        index = np.arange(len(scores))

        # Creating the figure and axes
        fig, ax = plt.subplots()

        # Creating 2 bars
        bar1 = ax.bar(index, value1, bar_width, label= label1, color='purple')
        bar2 = ax.bar(index + bar_width, value2, bar_width, label= label2, color='orange')

        # Adding labels, title, and legend
        ax.set_xlabel('Well-being Score')
        ax.set_ylabel('Number of adolescents')
        ax.set_title(title + field)
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(scores)
        ax.legend()

        # Displaying the chart
        plt.show()

bar_chart(df_g0, df_g1, 'Number of adolescents by Well-being Score and Gender: ', 'Otherwise', 'Male')
bar_chart(df_m0, df_m1, 'Number of adolescents by Well-being Score and Minority: ', 'Majority', 'Otherwise')
bar_chart(df_d0, df_d1, 'Number of adolescents by Well-being Score and Deprivation: ', 'Deprived', 'Otherwise')

























