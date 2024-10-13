import seaborn as sns
import pathlib

from A3_datawrangling import *

pathlib.Path('output/correlation/').mkdir(parents=True, exist_ok=True) 
pathlib.Path('output/scatter/').mkdir(parents=True, exist_ok=True) 

#Plot scatter for each well-being field
for wellbeing_field in wellbeing_fields:
    df = getDataFrame(wellbeing_field, False)
    X_cols = df.iloc[:,:-1].columns.values
    print(X_cols)
    for col in X_cols:
        scatter = sns.scatterplot(df, x=col, y =wellbeing_field)
        scatter.set_title(f'Scatter Plot: {wellbeing_field} vs {col}')
        scatter.figure.savefig(f'output/scatter/{wellbeing_field}-{col}.png')
        scatter.figure.clf()


# Plot the matrix as a heatmap to check remove multicollinearity
corr = df2.corr()
ax = sns.heatmap(
    corr,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=False,
    annot=True
)
ax.figure.set_size_inches(12, 8)

# customise the labels
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
)

ax.figure.savefig(f'output/correlation/heatmapCorrel.png')
ax.figure.clf()