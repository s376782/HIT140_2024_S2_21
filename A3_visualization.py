import seaborn as sns
import pathlib

from A3_datawrangling import *

pathlib.Path('output/correlation/').mkdir(parents=True, exist_ok=True) 
pathlib.Path('output/scatter/').mkdir(parents=True, exist_ok=True) 

# compute the correlation matrix
for wellbeing_field in wellbeing_fields:
    df = getDataFrame(wellbeing_field, False)

    corr = df.corr()

    # plot the matrix as a heatmap
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

    ax.figure.savefig(f'output/correlation/{wellbeing_field}.png')
    ax.figure.clf()
    
    X_cols = df.iloc[:,:-1].columns.values
    for col in X_cols:
        scatter = sns.scatterplot(df, x=col, y=wellbeing_field)
        scatter.figure.savefig(f'output/scatter/{wellbeing_field}-{col}.png')
        scatter.figure.clf()
