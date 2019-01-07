def basiCard():
    return {
    "fulfillmentMessages": [
        {
        "text": {
            "text": [
            "Searcing for flights from OSL to CPH at 2019-01-07"
            ]
        }
        },
        {
        "card": {
            "title": "Searcing Momondo",
            "subtitle": "Searcing for flights from OSL to CPH at 2019-01-07",
            "imageUri": "https://www.aworldtotravel.com/wp-content/uploads/2014/06/momondo-travel-app-friend-compass-review-1050x704.jpg",
            "buttons": [
            {
                "text": "View results",
                "postback": "https://www.momondo.no/flight-search/OSL-CPH/2019-01-07T12:00:00+01:00/?sort=price_a"
            }
            ]
        }
        }
    ],
    "outputContexts": []
    }


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