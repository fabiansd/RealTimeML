
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

IMG_ROOT_PATH = os.path.join('static','plots')
PLOT_SIZE = (10,6)

def groupPlot(group,column,plot, IMG_PATH, df):
    # df = pd.read_csv(os.path.join('data','BFCleaned.csv'), index_col =0)


    print(IMG_PATH)
    print('\n')
    print(group, column)
    print('\n')

    # ax=plt.figure(figsize=PLOT_SIZE)

    # df.groupby(group)[column].sum().sort_values().plot(plot)
    # plt.ylabel(column)
    # plt.xlabel(group)
    
    ax=plt.figure(figsize=(12,6))

    print('fig')

    # table = df.groupby(group)[column].sum().sort_values().plot(plot)
    df.groupby(group)[column].sum().sort_values().plot(plot)
    print('group')
    
    plt.ylabel(column)
    plt.xlabel(group)

    plt.savefig(IMG_PATH)

    print('plot sved')


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

    if hue != '':
        sns.countplot(df[var],hue=df[hue],order=df[var].value_counts().index)
    else:
        sns.countplot(df[var],order=df[var].value_counts().index)

    plt.savefig(IMG_PATH)

