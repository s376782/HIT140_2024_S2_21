import pathlib
from A2_datawrangling import *

# y = np.array([35, 25, 25, 15])
mylabels = [1, 2, 3, 4, 5]

#def pie_chart(dfa):
#     for field in wellbeing_fields:
def draw_piechart(data, fields, title, output):
    for index, field in enumerate(fields):
        import matplotlib.pyplot as plt
        y = []
        total_percentage_3_4_5 = 0
        for i in mylabels:
            number_i = data.loc[data[field] == i].shape[0] 
            percentage_i = number_i/data.shape[0]*100
            print(number_i)
            print(percentage_i)
            y.append(number_i)
            if i in [3, 4, 5]:
                total_percentage_3_4_5 += percentage_i
#        plt.pie(y, labels = mylabels, startangle = 90)
        plt.pie(y, labels=mylabels, startangle=90, autopct='%1.1f%%')
        plt.legend(title=str(field), bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.title(title.format(field))
        # plt.show()
        plt.savefig(output.format(index, field))
        plt.clf()
        print(f"Total percentage of categories 3, 4, 5 for {field}: {total_percentage_3_4_5:.2f}%")

pathlib.Path('output/df_high_st').mkdir(parents=True, exist_ok=True) 
draw_piechart(df_high_st, wellbeing_fields,
            'Pie Chart for {0} score with high screening time group',
            'output/df_high_st/{0:02d}_{1}.png')
pathlib.Path('output/df_low_st').mkdir(parents=True, exist_ok=True) 
draw_piechart(df_low_st, wellbeing_fields,
            'Pie Chart for {0} score with low screening time group',
            'output/df_low_st/{0:02d}_{1}.png')

pathlib.Path('output/df_g1').mkdir(parents=True, exist_ok=True) 
draw_piechart(df_g1_wo_outliers, wellbeing_fields,
            'Pie Chart for {0} score with male gender group',
            'output/df_g1/{0:02d}_{1}.png')
pathlib.Path('output/df_g0').mkdir(parents=True, exist_ok=True) 
draw_piechart(df_g0_wo_outliers, wellbeing_fields,
            'Pie Chart for {0} score with otherwise gender group',
            'output/df_g0/{0:02d}_{1}.png')

pathlib.Path('output/df_m1').mkdir(parents=True, exist_ok=True) 
draw_piechart(df_m1_wo_outliers, wellbeing_fields,
            'Pie Chart for {0} score with majority minority group',
            'output/df_m1/{0:02d}_{1}.png')
pathlib.Path('output/df_m0').mkdir(parents=True, exist_ok=True) 
draw_piechart(df_m0_wo_outliers, wellbeing_fields,
            'Pie Chart for {0} score with otherwise minority group',
            'output/df_m0/{0:02d}_{1}.png')

pathlib.Path('output/df_d1').mkdir(parents=True, exist_ok=True) 
draw_piechart(df_d1_wo_outliers, wellbeing_fields,
            'Pie Chart for {0} score with deprived group',
            'output/df_d1/{0:02d}_{1}.png')
pathlib.Path('output/df_d0').mkdir(parents=True, exist_ok=True) 
draw_piechart(df_d0_wo_outliers, wellbeing_fields,
            'Pie Chart for {0} score with otherwise deprived group',
            'output/df_d0/{0:02d}_{1}.png')
