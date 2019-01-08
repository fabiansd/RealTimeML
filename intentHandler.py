import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import plotly.plotly as py

import os

from gen_HTML import gen_HTML_plot

IMG_ROOT_PATH = os.path.join('static','plots')

def generateReportPlot(params):

### GENERATE PLOTS #####

    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05),)

    plt.ylim(-2,2)

    IMG_PATH = os.path.join(IMG_ROOT_PATH,'generateReportPlot.jpg')

    plt.savefig(IMG_PATH)

### GENERATE HTML SCRIPT

    gen_HTML_plot(header= 'Plot report from date to date', IMG_PATH = IMG_PATH)

    return {'fulfillmentText': 'Report from date to date is available at http://127.0.0.1:5000/report'}



def generateCategoriesPlot(params):
    return {'fulfillmentText': 'Report kategori'}


