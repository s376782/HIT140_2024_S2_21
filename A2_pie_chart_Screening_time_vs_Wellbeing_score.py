import matplotlib.pyplot as plt
import numpy as np
from A2_datawrangling import *

# y = np.array([35, 25, 25, 15])
mylabels = [1, 2, 3, 4, 5]

#def pie_chart(dfa):
#     for field in wellbeing_fields:
def draw_piechart(data, fields):
    for field in fields:
        y = []
        for i in mylabels:
            number_i = data.loc[data[field] == i].shape[0] 
            percentage_i = number_i/data.shape[0]*100
            print(number_i)
            print(percentage_i)
            y.append(number_i)
#        plt.pie(y, labels = mylabels, startangle = 90)
        plt.pie(y, labels=mylabels, startangle=90, autopct='%1.1f%%')
        plt.legend(title=str(field), bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.title(f"Pie Chart for {field}")
        plt.show()

draw_piechart(df_low_st, wellbeing_fields)
draw_piechart(df_high_st, wellbeing_fields)

