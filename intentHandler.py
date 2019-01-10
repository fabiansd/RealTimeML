import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.plotly as py

import os

from gen_HTML import gen_HTML_report
from responses import basiCard
from plotFunctions import groupPlot, countPlot, kakePlot

import time

# Path for the image storage
IMG_ROOT_PATH = os.path.join('static','plots')

# Every intent has a designated function that generates the relevant report and 
# saves the plats as an images with the same name as the function. Then the 
# HTML report site is updated. Finally a basicard response is returned to Dialogflow
def generateGroupbyPlot(params, df):

    
### GENERATE PLOTS ###

    # Her må params matches opp
    # plot( group , column, type plot)
    gruppe = params['gruppe']
    kolonne = params['kolonne']
    IMG_PATH = os.path.join(IMG_ROOT_PATH,str(time.time()) + '.jpg')

    groupPlot(gruppe,kolonne,'bar',IMG_PATH, df)

    # fig.savefig(IMG_PATH)

### GENERATE HTML SCRIPT ###

    gen_HTML_report(header= 'Gruppering plot', sub_header=f'{kolonne} gruppert i {gruppe}', IMG_PATH = IMG_PATH)

### RETURN BASICARD RESPONSE ###

    return basiCard(msg=f'{kolonne} gruppert i {gruppe}', title='Report')


def generateKakePlot(params, df):

    
### GENERATE PLOTS ###

    gruppe = params.get('gruppe')
    IMG_PATH = os.path.join(IMG_ROOT_PATH,str(time.time()) + '.jpg')

    kakePlot(gruppe, IMG_PATH, df)


### GENERATE HTML SCRIPT ###

    gen_HTML_report(header= 'Gruppering plot', sub_header=f'Antall transaksjoner fordelt i {gruppe}', IMG_PATH = IMG_PATH)

### RETURN BASICARD RESPONSE ###

    return basiCard(msg=f'Antall transaksjoner fordelt i {gruppe}', title='Report')


def generateCountPlot(params, df):

### GENERATE PLOTS ###
    gruppe = params.get('gruppe')
    hue = params.get('hue')

    IMG_PATH = os.path.join(IMG_ROOT_PATH,str(time.time()) + '.jpg')

    countPlot(gruppe, hue, IMG_PATH, df)

    if hue != '':
        comment = f'Antall transaksjoner fordelt i {gruppe}, kategorisert i {hue}'
    else:
        comment = f'Antall transaksjoner fordelt i {gruppe}'


### GENERATE HTML SCRIPT ###

    gen_HTML_report(header= 'Gruppering plot', sub_header=comment, IMG_PATH = IMG_PATH)

### RETURN BASICARD RESPONSE ###

    return basiCard(msg=comment, title='Report')


def datainfo():

    return basiCard(msg='Link to dataset information', title='Report', url="https://2226d3ee.ngrok.io/datainfo")