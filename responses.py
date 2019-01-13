
# A basicard response in JSON form
def basiCard(msg = "Report link to generated report", title = 'Report site', subtitle = "", url=""):

    return {"fulfillmentMessages":[{"text":{"text":[msg]}},\
    {"card":{"title":title,"subtitle":"",\
    "imageUri":"https://www.maxpixel.net/static/photo/1x/Report-Accounting-Business-Paper-Financial-Graph-3076855.jpg",\
    "buttons":[{"text":"View","postback":url\
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
                    "url": url
                    }
                }
            }
        }
    }