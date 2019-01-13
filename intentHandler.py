import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.plotly as py

import os

from gen_HTML import gen_HTML_report
from responses import basiCard
from plotFunctions import barPlot, countPlot, kakePlot, purchasePlot

import time

# Path for the image storage
URL = "https://9134f82e.ngrok.io"
URL_REPORT = os.path.join(URL,'report')
URL_DATAINFO = os.path.join(URL,'datainfo')

IMG_ROOT_PATH = os.path.join('static','plots')

# Every intent has a designated function that generates the relevant report and 
# saves the plats as an images with the same name as the function. Then the 
# HTML report site is updated. Finally a basicard response is returned to Dialogflow
def generateGroupbyPlot(params, df):
    
### GENERATE PLOTS ###

    x = params.get('x')
    # y = params.get('y')
    hue= params.get('hue')
    IMG_PATH = os.path.join(IMG_ROOT_PATH,str(x)+str(hue) + '_salg_bar.jpg')

    if os.path.isfile(IMG_PATH) != True:
        purchasePlot(x,hue,IMG_PATH, df)

### GENERATE HTML SCRIPT ###
    if hue == '':
        comment = f'Salg fordelt over {x}'
    else:
        comment = f'Salg fordelt over {x}, kategorisert i {hue}'

    gen_HTML_report(header= 'Gruppering plot', sub_header=comment, IMG_PATH = IMG_PATH)

### RETURN BASICARD RESPONSE ###

    print('bar plot entered')
    return basiCard(msg=comment, title='Report', url=URL_REPORT)



def generatePurchasePlot(params, df):
    print('bar plot entered')
    
### GENERATE PLOTS ###

    x = params.get('x')
    y = params.get('y')
    hue= params.get('hue')
    IMG_PATH = os.path.join(IMG_ROOT_PATH,str(x)+str(y)+str(hue) + '_bar.jpg')

    if os.path.isfile(IMG_PATH) != True:
        barPlot(x,y,hue,IMG_PATH, df)

### GENERATE HTML SCRIPT ###
    if hue == '':
        comment = f'{y} fordelt over {x}'
    else:
        comment = f'{y} fordelt over {x}, kategorisert i {hue}'

    gen_HTML_report(header= 'Gruppering plot', sub_header=comment, IMG_PATH = IMG_PATH)

### RETURN BASICARD RESPONSE ###

    print('bar plot entered')
    return basiCard(msg=comment, title='Report', url=URL_REPORT)


def generateKakePlot(params, df):
### GENERATE PLOTS ###

    gruppe = params.get('gruppe')
    IMG_PATH = os.path.join(IMG_ROOT_PATH,str(gruppe) + '_kake.jpg')

    if os.path.isfile(IMG_PATH) != True:
        kakePlot(gruppe, IMG_PATH, df)


### GENERATE HTML SCRIPT ###

    gen_HTML_report(header= 'Gruppering plot', sub_header=f'Antall transaksjoner fordelt i {gruppe}', IMG_PATH = IMG_PATH)

### RETURN BASICARD RESPONSE ###

    return basiCard(msg=f'Antall transaksjoner fordelt i {gruppe}', title='Report', url=URL_REPORT)


def generateCountPlot(params, df):

### GENERATE PLOTS ###
    gruppe = params.get('gruppe')
    hue = params.get('hue')

    IMG_PATH = os.path.join(IMG_ROOT_PATH,str(gruppe)+str(hue) + '_count.jpg')
    if os.path.isfile(IMG_PATH) != True:
        countPlot(gruppe, hue, IMG_PATH, df)

    if hue != '':
        comment = f'Antall transaksjoner fordelt i {gruppe}, kategorisert i {hue}'
    else:
        comment = f'Antall transaksjoner fordelt i {gruppe}'


### GENERATE HTML SCRIPT ###

    gen_HTML_report(header= 'Gruppering plot', sub_header=comment, IMG_PATH = IMG_PATH)

### RETURN BASICARD RESPONSE ###

    return basiCard(msg=comment, title='Report', url=URL_REPORT)

def generateCorr(params, df):

    IMG_PATH = os.path.join(IMG_ROOT_PATH,'korrelasjon.jpg')

    if os.path.isfile(IMG_PATH) != True:

        df_pred = pd.read_csv(os.path.join('data','BFCleaned.csv'), index_col =0)
        df_pred['Alder'] = df_pred['Alder'].map({'0-17': 0, '18-25': 1, '26-35': 2, '36-45': 3, '46-50': 4, '51-55': 5, '55+': 6})
        df_pred['Kjønn'] = df_pred['Kjønn'].map({'M': 0,'F': 1})
        df_pred['By'] = df_pred['By'].map({'A': 0,'B': 1,'C': 2})
        df_pred['Boperiode_i_by'] = df_pred['Boperiode_i_by'].map({'0': 0, '1': 1, '2': 2, '3': 3, '4+': 4})


        import seaborn as sns
        corrmat = df_pred[['Kjønn', 'Alder', 'Yrke', 'By',
        'Boperiode_i_by', 'Sivilstatus', 'Produkt_kategori',
        'Salg']].corr()
        fig,ax = plt.subplots(figsize = (10,6))
        sns.heatmap(corrmat, vmax=.8, square=True)

        plt.savefig(IMG_PATH)

    gen_HTML_report(header= 'Korrelasjonsmatrise', sub_header='', IMG_PATH = IMG_PATH)

### RETURN BASICARD RESPONSE ###

    return basiCard(msg='Korrelasjonsmatrise', title='Report', url=URL_REPORT)

def datainfo():

    return basiCard(msg='Link to dataset information', title='Report', url=URL_DATAINFO)