import requests
import json, demjson
import pandas as pd
from pandas import Series, DataFrame
from pandas.io.json import json_normalize

def get_lowest_price_from_naver_flight(querystring):

    # url = "https://store.naver.com/flights/api/realtime/international"
    # print(url)
    # print(headers)
    # print(querystring)
    #response = requests.request("GET", url, headers=json.loads(headers), params=json.loads(querystring))

    headers = {
        'host': "store.naver.com",
        'connection': "keep-alive",
        'accept': "application/json, text/plain, */*",
        'authorization': "Basic bXlib3R0bGU6d2F0ZXJicm93bg==",
        'accept-encoding': "gzip, deflate, sdch, br",
        'accept-language': "ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4",
        'cache-control': "no-cache",
        'postman-token': "58973081-9584-a272-bab2-e7e86c3a7a82"
    }

    # print(querystring)
    # print(headers)
    # response = requests.request("GET", querystring, headers=headers)
    # response = requests.request("GET", url, headers=headers, params=querystring)
    response = requests.get(querystring, headers=headers)
    raw_data = json.loads(response.text)

    df = json_normalize(raw_data['searchResult']['fareGroupList'])
    rawlist = list(df.T[0])

    alllist = list()
    for x in range(0, len(rawlist)):
        alllist.extend(rawlist[x])

    templist = list()
    for x in range(0, len(alllist)):
        if(alllist[x]['status'] == 'HK'):
            templist.extend(alllist[x]['fareList'])

    dataresult = DataFrame()

    for x in range(0, len(templist)):
        temp = pd.DataFrame.from_dict(templist[x], orient='index')
        dataresult = dataresult.append(temp)

    lowest_price = int(dataresult.T['SaleFare'].T.values[0][0])
    for price in dataresult.T['SaleFare'].T.values:
        # print(str(lowest_price) + ' : ' + str(price[0]))
        if lowest_price > int(price[0]):
            lowest_price = int(price[0])

    return lowest_price

# url = "https://store.naver.com/flights/api/realtime/international"
# querystring = {"Adt":"1","Chd":"0","ECITY1":"CDG","ECITY2":"ICN","FareType":"Y","Inf":"0","SCITY1":"ICN","SCITY2":"CDG","SDATE1":"2017.06.05.","SDATE2":"2017.06.11.","TRIP":"RT","Where":"mobile"}
# headers = {
#     "host": "store.naver.com",
#     "connection": "keep-alive",
#     "accept": "application/json, text/plain, */*",
#     "authorization": "Basic bXlib3R0bGU6d2F0ZXJicm93bg==",
#     "accept-encoding": "gzip, deflate, sdch, br",
#     "accept-language": "ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4",
#     "cache-control": "no-cache"
#     }
#
# querystring = {'SCITY1': 'ICN', 'Where': 'mobile', 'Adt': '1', 'SCITY2': 'CDG', 'ECITY1': 'CDG', 'Chd': '0', 'SDATE2': '2017.06.11.', 'Inf': '0', 'ECITY2': 'ICN', 'SDATE1': '2017.06.05.', 'TRIP': 'RT', 'FareType': 'Y'}
# headers = {'connection': 'keep-alive', 'authorization': 'Basic bXlib3R0bGU6d2F0ZXJicm93bg==', 'accept-language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4', 'cache-control': 'no-cache', 'host': 'store.naver.com', 'accept': 'application/json, text/plain, */*', 'accept-encoding': 'gzip, deflate, sdch, br'}
# lowest_price = get_lowest_price_from_naver_flight(url, headers, querystring)
# print(lowest_price)