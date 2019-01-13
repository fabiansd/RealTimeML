
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

IMG_ROOT_PATH = os.path.join('static','plots')
PLOT_SIZE = (10,6)

def barPlot(x, y, hue, IMG_PATH, df):
    # df = pd.read_csv(os.path.join('data','BFCleaned.csv'), index_col =0)

    fig1, ax1 = plt.subplots(figsize=PLOT_SIZE)

    if hue != '':
        sns.barplot(x=x, y=y, hue=hue, data=df)

    else:
        sns.barplot(x=x, y=y, data=df)

    plt.savefig(IMG_PATH)

def purchasePlot(x, hue, IMG_PATH, df):
    # df = pd.read_csv(os.path.join('data','BFCleaned.csv'), index_col =0)

    fig1, ax1 = plt.subplots(figsize=PLOT_SIZE)

    if hue != '':
        df.groupby([x,hue])['Salg'].sum().plot('barh')

    else:
        df.groupby(x)['Salg'].sum().plot('bar')

    plt.ylabel('Salg i dollar (k)')
    plt.savefig(IMG_PATH)



# IMG_ROOT_PATH = os.path.join('static','plots')
# IMG_PATH = os.path.join(IMG_ROOT_PATH,'generateGroupbyPlot.jpg')
# groupPlot('Alder','Salg','bar', IMG_PATH)

def kakePlot(var, IMG_PATH, df):
    # df = pd.read_csv(os.path.join('data','BFCleaned.csv'), index_col =0)
    print(df[var].head())
    fig1, ax1 = plt.subplots(figsize=(12,7))
    ax1.pie(df[var].value_counts(), labels=df[var].unique(), autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')  
    plt.tight_layout()
    plt.legend()
 
    plt.savefig(IMG_PATH)

def countPlot(var, hue, IMG_PATH, df):
    # df = pd.read_csv(os.path.join('data','BFCleaned.csv'), index_col =0)

    fig1, ax1 = plt.subplots(figsize=PLOT_SIZE)
    print(df[var].unique())

    if hue != '':
        sns.countplot(df[var],hue=df[hue])
    else:
        sns.countplot(df[var])

    plt.savefig(IMG_PATH)

