import requests, json, os, time, random
from math import floor
from requests.exceptions import HTTPError
import bikes
import datetime

def time_parser(secs):
    t=secs%60
    mins=int((secs-t)/60)
    str="{}:{:02d}".format(mins,t)
    return str

def cur_time_in_secs():
    n=datetime.datetime.now().time()
    return n.hour*60*60+n.minute*60+n.second

def get_zyk():
    url="https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"
    headers={'Content-Type':'application/graphql'}
    dataString=""
    for bike in bikes.LST:
        try:
            response = requests.post(url,data=bike,headers=headers,timeout=10)
        except HTTPError as http_err:
            print('HTTP error occurred: ' + http_err)
            return "HSL API connection failed"
        except Exception as err:
            print('Other error occurred: ' + err)
            return "HSL API connection failed"
        else:
            x = response.json()
            drop=x.get("data",{}).get("bikeRentalStation",{}).get("allowDropoff","False")
            name=x.get("data",{}).get("bikeRentalStation",{}).get("name","")
            bks=x.get("data",{}).get("bikeRentalStation",{}).get("bikesAvailable","0")
            sps=x.get("data",{}).get("bikeRentalStation",{}).get("spacesAvailable","0")+bks
            if drop:
                dataString=dataString+ "{}: {}/{}.\n".format(name,bks,sps)
            else:
                dataString=dataString+"{}: closed.\n".format(name)
    return(dataString)

def get_dös():
    buslist={}
    url="https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"
    headers={'Content-Type':'application/graphql'}
    dataString=""
    for stop in {bikes.S1,bikes.S2}:
        try:
            response = requests.post(url,data=stop,headers=headers,timeout=10)
        except HTTPError as http_err:
            print('HTTP error occurred: ' + http_err)
            return "HSL API connection failed"
        except Exception as err:
            print('Other error occurred: ' + err)
            return "HSL API connection failed"
        else:
            try:
                x = response.json()
            except:
                return("Query failed.")
            busses=((x.get("data",{}).get("stop",{}).get("stoptimesWithoutPatterns",{})))
            for bus in busses:
                diff=bus["realtimeArrival"]-cur_time_in_secs()
                if diff<=0:
                    tim="0:00"
                else:
                    tim=time_parser(diff)
                if bus["realtime"]:
                    tim=tim+"✅"
                if not bus["trip"]["route"]["shortName"] in buslist:
                    buslist[bus["trip"]["route"]["shortName"]]=[tim]
                else:
                    buslist[bus["trip"]["route"]["shortName"]].append(tim)
    for k in buslist:
        dataString="{}{}:  ".format(dataString,k)
        for t in buslist[k]:
            dataString="{}{}, ".format(dataString,t)
        dataString="{}\n".format(dataString)
    return(dataString)

