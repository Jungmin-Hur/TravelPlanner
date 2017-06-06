import requests
import json, demjson
import pandas as pd
from pandas import Series, DataFrame
from pandas.io.json import json_normalize

url = "https://store.naver.com/flights/api/realtime/international"

querystring = {"Adt":"1","Chd":"0","ECITY1":"CDG","ECITY2":"ICN","FareType":"Y","Inf":"0","SCITY1":"ICN","SCITY2":"CDG","SDATE1":"2017.07.05.","SDATE2":"2017.07.11.","TRIP":"RT","Where":"mobile"}

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

response = requests.request("GET", url, headers=headers, params=querystring)

raw_data = json.loads(response.text)

df = json_normalize(raw_data['searchResult']['fareGroupList']);
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

print('==1')
print(dataresult.T['SaleFare'])
print('==2')
print(dataresult.T['SaleFare'].T)
print('==3')
print((dataresult.T['SaleFare'].T).loc[0])
print('==4')
print((dataresult.T['SaleFare'].T).loc[1])
print('==5')
