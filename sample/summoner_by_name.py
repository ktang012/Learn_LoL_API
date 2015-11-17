# Sample usage of summoner-1.4_sample
import requests
import json
import time
import API_key

my_key = API_key.GetKey()

def InputRegion():
    region = input("""
        Enter region:
        BR, EUNE, EUW, KR, LAN, LAS, NA, OCE, RU, TR
        \r""")
    return region

def InputSummonerName():
    summoner_name = input("""
        Enter summoner name:
        \r""")
    return summoner_name

def GetData(region, summoner_name_html):
    call = "https://" + region + ".api.pvp.net/api/lol/" + region + \
           "/v1.4/summoner/by-name/" + summoner_name_html + my_key
    try:
        my_request = requests.get(call)

    except requests.exceptions.ConnectionError as error:
        print("Invalid summoner name or region")
        exit()

    my_data = json.loads(my_request.text)
    return my_data

def PrintData(summoner_name, data):
    for i in data[summoner_name].keys():
        print("%s: %s" % (i.title(), data[summoner_name][i]))

def GetSummonerID(summoner_name, data):
    return data[summoner_name]['id']

def GetSummonerName(summoner_name, data):
    return data[summoner_name]['name']

def GetProfileIconID(summoner_name, data):
    return data[summoner_name]['profileIconId']

def GetRawRevisionDate(summoner_name, data):
    """Last modified icon change, play tutorial, play game, summoner name change
       in epoch milliseconds"""
    return data[summoner_name]['revisionDate']

def GetRevisionDate(summoner_name, data):
    """Last modified icon change, play tutorial, play game, summoner name change
       in a %Y-%m-%d"""
    date = GetRawRevisionDate(summoner_name, data)
    return time.strftime('%Y-%m-%d', time.gmtime(date/1000.0))

def GetSummonerLevel(summoner_name, data):
    return data[summoner_name]['summonerLevel']

def main():
    region = InputRegion()
    raw_summoner_name = InputSummonerName()
    summoner_name = raw_summoner_name.replace(" ", "")
    summoner_name_html = raw_summoner_name.replace(" ", "%20")
    my_data = GetData(region, summoner_name_html)
    PrintData(summoner_name, my_data)

if __name__ == '__main__':
    main()
