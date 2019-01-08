REPORT_URL = "https://2226d3ee.ngrok.io/report"

def basiCard(msg = "Report link to generated report", title = 'Report site', subtitle = ""):

    return {"fulfillmentMessages":[{"text":{"text":[msg]}},\
    {"card":{"title":title,"subtitle":"",\
    "imageUri":"https://www.maxpixel.net/static/photo/1x/Report-Accounting-Business-Paper-Financial-Graph-3076855.jpg",\
    "buttons":[{"text":"View report","postback":REPORT_URL\
    }]}}],"outputContexts":[]}

def suggestion(response, suggestions = [{ "title": "25"}, { "title": "45" }, {"title": "Never mind"}]):
    return {
    "payload": {
            "google": {
            "expectUserResponse": True,
            "richResponse": {
                    "items": [
                    {
                        "simpleResponse": {
                        "textToSpeech": response
                        }
                    }
                    ],
                    "suggestions": suggestions,
                    "linkOutSuggestion": {
                    "destinationName": "Website",
                    "url": "https://assistant.google.com"
                    }
                }
            }
        }
    }