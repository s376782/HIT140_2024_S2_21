import seaborn as sns
import matplotlib.pyplot as plt
import pathlib

from A3_datawrangling import *

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

    # customise the labels
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right'
    )

    pathlib.Path('output/correlation/').mkdir(parents=True, exist_ok=True) 
    plt.savefig(f'output/correlation/{wellbeing_field}.png')
    plt.clf()

    X_cols = df.iloc[:,:-1].columns.values
    for col in X_cols:
        plt.scatter(x=df[col], y=df[wellbeing_field])
        plt.xlabel(col)
        plt.ylabel(wellbeing_field)

        pathlib.Path(f'output/scatter/{wellbeing_field}').mkdir(parents=True, exist_ok=True) 
        plt.savefig(f'output/scatter/{wellbeing_field}/{col}.png')
        plt.clf()
