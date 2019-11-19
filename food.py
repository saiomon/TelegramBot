import requests, re
from requests.exceptions import HTTPError,Timeout
from datetime import datetime,date,timedelta

def por(d=date.today()):
    try:
        response=requests.get("http://por.fi/Menu-Pitajanmaki",timeout=10)
    except Timeout:
        return "Site not responding"
    except HTTPError as http_err:
        print('HTTP error occurred: ' + http_err)
    except Exception as err:
        print('Other error occurred: ' + err)
    else:
        sep=str(d.day)+"."+str(d.month)
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

def por_v(d=date.today()):
    try:
        response=requests.get("http://por.fi/Menu-Vuosaari",timeout=10)
    except Timeout:
        return "Site not responding"
    except HTTPError as http_err:
        print('HTTP error occurred: ' + http_err)
    except Exception as err:
        print('Other error occurred: ' + err)
    else:
        sep=str(d.day)+"."+str(d.month)+"."
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

def get_dates(fromD=date.today()):
    ds=[]
    try:
        response=requests.get("http://por.fi/Menu-Pitajanmaki",timeout=10)
    except Timeout:
        return "Site not responding"
    except HTTPError as http_err:
        print('HTTP error occurred: ' + http_err)
    except Exception as err:
        print('Other error occurred: ' + err)
    else:
        for i in range(7):
            tst=fromD.replace(day=fromD.day+i)
            sep=str(tst.day)+"."+str(tst.month)
            if sep in response.text:
                ds.append(sep)
    return ds

def get_dates_v(fromD=date.today()):
    ds=[]
    try:
        response=requests.get("http://por.fi/Menu-Vuosaari",timeout=10)
    except Timeout:
        return "Site not responding"
    except HTTPError as http_err:
        print('HTTP error occurred: ' + http_err)
    except Exception as err:
        print('Other error occurred: ' + err)
    else:
        for i in range(7):
            tst=fromD.replace(day=fromD.day+i)
            sep=str(tst.day)+"."+str(tst.month)
            if sep in response.text:
                ds.append(sep)
    return ds


def ravioli():
    for i in range(3):
        r=por(date.today()+timedelta(days=i)).lower()
        if "raviol" in r:
            if i==0:
                return "Tänään on raviolipäivä!!"
            elif i==1:
                return "Huomenna raviolia!"
            elif i==2:
                return "Ylihuomenna raviolia!"
    return None
