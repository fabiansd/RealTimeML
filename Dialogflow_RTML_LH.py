
# import flask dependencies
from flask import Flask, request, make_response, jsonify, render_template
import requests
import json
from datetime import datetime


from werkzeug.debug import DebuggedApplication
# from gen_HTML import generate_HTML_report
from gen_PLOTS import *
from responses import *



### INTENTS ####
PLOT_NUMBERS_INTENT = 'report.plot'
PLOT_CATEGORIES_INTENT = 'report.categories'

app = Flask(__name__)
appDebug = DebuggedApplication(app, evalex=True)

### switch case for calling correct intent handler
def handleWebhook(intent, params):

    if intent == PLOT_NUMBERS_INTENT: return generateReportPlot(params)
    elif intent == PLOT_CATEGORIES_INTENT: return generateCategoriesPlot(params),
    elif 
    else: return {'fulfillmentText': 'No intent handler found'}

# default route
@app.route('/')
def index():

    return render_template("sampleReport.html")


@app.route('/webhook', methods=['POST','GET'])
def webhook():

    # build a request object
    req = request.get_json(force=True)


    # print(req)
    # fetch action from json
    # print('\n\n\n')

    intent = req.get('queryResult').get('intent').get('displayName')
    params = req.get('queryResult').get('parameters')

    print(f'intent: {intent}')
    print(f'params: {params}')

    response = {'fulfillmentText': 'Hello from Flask webhook.'}

    response = handleWebhook(intent, params)
    print(response)
    
    return jsonify(response)
    # return jsonify(handleWebhook(intent, params))


# Host report 
@app.route('/report', methods=['GET'])
def report():
    return render_template('report.html')


@app.route('/wet', methods = ['GET','POST'])
def getWeather():

    by = request.json['context']['by']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={by},no&appid=f7ed6fec949211b9148f103fec18c58d'

    req = requests.get(url).json()

    print(req)

    try:
        description = req['weather'][0]['description']
        tempKelvin = req['main']['temp']
        sunrise = req['sys']['sunrise']
        sunset = req['sys']['sunset']

        sunriseDT = datetime.utcfromtimestamp(sunrise).strftime('%Y-%m-%d %H:%M:%S')
        sunsetDT = datetime.utcfromtimestamp(sunset).strftime('%Y-%m-%d %H:%M:%S')

    except KeyError:
        return jsonify(reply=f'Fant ikke data på {by}')
        
    image_obj = {
        # 'image': "https://media.giphy.com/media/FhOCTD5CzzAm4/giphy.gif",
        'image': "https://i.pinimg.com/originals/2c/3a/d3/2c3ad3b60885d9864b48366d45143fb1.gif",
        'image_alt_text': "Simpson GIF",
        'reply': f'Det vil bli {description} og {tempKelvin}K \n\nSolen går opp {sunriseDT} og ned {sunsetDT}',
        'buttons':   [ 
            {
                "button_type": "link",
                "label": "Source link",
                "value": url
            }
        ]
    }
    return jsonify(image_obj)

# run the app
if __name__ == '__main__':
   app.run(debug=True)