import random, requests,os,json
from datetime import datetime,timedelta
def new_time():
        return timedelta(hours=random.randint(3,23),minutes=random.randint(0,59))

def get_jee():
    s=random.randint(0,2)
    if s==0:
        return get_math()
    if s==1:
        return get_quate()
    if s==2:
        return get_joke()


def get_math():
    key=os.environ.get("RAPID_API_KEY", None)
    url = "https://numbersapi.p.rapidapi.com/random/trivia"
    querystring = {"max":"10000","fragment":"true","min":"0","json":"true"}

    headers = {
        'x-rapidapi-host': "numbersapi.p.rapidapi.com",
        'x-rapidapi-key': key
        }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
    except requests.exceptions.HTTPError as http_err:
        print('HTTP error occurred: ' + http_err)
        return "Weather API connection failed"
    except Exception as err:
        print('Other error occurred: ' + err)
        return "Weather API connection failed"
    else:
        x=response.json()
        return("{}: {}".format(x.get("number",""),x.get("text","")))

def get_joke():
    url="https://icanhazdadjoke.com/"
    headers={
        'accept': 'text/plain',
        'User-Agent':'ErppaBot'
    }
    try:
        response = requests.request("GET", url, headers=headers)
    except requests.exceptions.HTTPError as http_err:
        print('HTTP error occurred: ' + http_err)
        return "Weather API connection failed"
    except Exception as err:
        print('Other error occurred: ' + err)
        return "Weather API connection failed"
    else:
        return response.text


def get_quate():
    db=readfile()
    if db:
        print("Saved quetes found")
    else:
        print("Get quates")
        key=os.environ.get("RAPID_API_KEY", None)

        url = "https://andruxnet-random-famous-quotes.p.rapidapi.com/"
        querystring = {"cat":"famous","count":"10"}

        headers = {
            'x-rapidapi-host': "andruxnet-random-famous-quotes.p.rapidapi.com",
            'x-rapidapi-key': key,
            'User-Agent': 'Erppa'
            }

        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
        except requests.exceptions.HTTPError as http_err:
            print('HTTP error occurred: ' + http_err)
            return "Weather API connection failed"
        except Exception as err:
            print('Other error occurred: ' + err)
            return "Weather API connection failed"
        else:
            print(response.text)
            db=response.json()

    #print(db[0])
    str="{}\n\t-{}".format(db[0].get("quote",""),db[0].get("author","None"))
    del db[0]
    savefile(db)
    return str

def savefile(data):
    try:
        with open('quate.json', 'w+') as outfile:
            outfile.write(json.dumps(
                                data,
                                indent=4,
                                sort_keys=True))
    except (IOError, TypeError) as e:
        print(data)
        print('Saving the data failed!!')
        print(e)

def readfile():
    try:
        print("Loading quates...")
        with open('quate.json', 'r') as infile:
            data = json.load(infile)
            print("quate.json loaded!")
    except IOError:
        print('No quate.json file found!')
    except json.decoder.JSONDecodeError:
        print('Could not parse file!')
    else:
        return data
    return False
    