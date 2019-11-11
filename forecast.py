import os, requests
from requests.exceptions import HTTPError

def forecast(coord="60.179442,24.826689"):
    accessKey = os.environ.get("WEATHER_API_KEY", None)
    if accessKey == None:
        print("You must set the weather api access key to the environment variable WEATHER_API_KEY before running")
        return "Bot is missing weather api key"
    base_url = "https://api.darksky.net/forecast/"
    complete_url = base_url + accessKey + "/" + coord  + "?units=si&lang=fi"
    try:
        response = requests.get(complete_url)
    except HTTPError as http_err:
        print('HTTP error occurred: ' + http_err)
        return "Weather API connection failed"
    except Exception as err:
        print('Other error occurred: ' + err)
        return "Weather API connection failed"
    else:
        x = response.json()
        return x.get('currently').get('summary')+" ja "+str(x.get('currently').get('temperature')) +"°C nyt.\n"+x.get('hourly').get('summary')+"\n"+x.get('daily').get('summary')
