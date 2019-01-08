import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import plotly.plotly as py

import os

from gen_HTML import gen_HTML_report
from responses import basiCard

# Path for the image storage
IMG_ROOT_PATH = os.path.join('static','plots')

# Every intent has a designated function that generates the relevant report and 
# saves the plats as an images with the same name as the function. Then the 
# HTML report site is updated. Finally a basicard response is returned to Dialogflow
def generateReportPlot(params):

### GENERATE PLOTS ###

    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05),)

    plt.ylim(-2,2)

    IMG_PATH = os.path.join(IMG_ROOT_PATH,'generateReportPlot.jpg')

    plt.savefig(IMG_PATH)

### GENERATE HTML SCRIPT ###

    gen_HTML_report(header= 'Plot report from date to date', IMG_PATH = IMG_PATH)

### RETURN BASICARD RESPONSE ###

    return basiCard(msg='Report to date report', title='Date report')



def generateCategoriesPlot(params):
    return basiCard(msg='Report to categorical report', title='Category report')


