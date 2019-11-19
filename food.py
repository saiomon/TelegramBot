import requests, re
from requests.exceptions import HTTPError,Timeout
from datetime import datetime

def por(date=datetime.now()):
    try:
        response=requests.get("http://por.fi/Menu-Pitajanmaki",timeout=10)
    except Timeout:
        return "Site not responding"
    except HTTPError as http_err:
        print('HTTP error occurred: ' + http_err)
    except Exception as err:
        print('Other error occurred: ' + err)
    else:
        sep=str(datetime.now().day)+"."+str(datetime.now().month)
        dataString=sep+'\n'
        txt=response.text
        if sep in txt:
            txt=txt.split('<div id="Printable" class="printable">')[1].split(sep)[1].split("5.60")[0]
            txt=txt.replace("<br />","\n").replace("&nbsp","").replace(";","").replace("&ouml","ö").replace("&auml","ä")+"5.60"
            txt=remove_tags(txt)
            dataString=dataString+txt
        else:
            dataString=dataString+"Not available."
    return dataString

def por_v():
    try:
        response=requests.get("http://por.fi/Menu-Vuosaari",timeout=10)
    except Timeout:
        return "Site not responding"
    except HTTPError as http_err:
        print('HTTP error occurred: ' + http_err)
    except Exception as err:
        print('Other error occurred: ' + err)
    else:
        sep=str(datetime.now().day)+"."+str(datetime.now().month)+"."
        dataString=sep
        txt=response.text
        if sep in txt:
            txt=txt.split('<div id="Printable" class="printable">')[1].split(sep)[1].split("0.85")[0]
            txt=txt.replace("<br />","\n").replace("&nbsp","").replace(";","").replace("&ouml","ö").replace("&auml","ä")+"0.85"
            txt=remove_tags(txt)
            dataString=dataString+txt
        else:
            dataString=dataString+"Not available."
    return dataString

def remove_tags(txt):
    clean=re.compile('<.*?>')
    return re.sub(clean,'',txt)
