# import requests
# import json
#
# url = "https://store.naver.com/flights/api/realtime/international"
#
# querystring = {"Adt":"1","Chd":"0","ECITY1":"CDG","ECITY2":"ICN","FareType":"Y","Inf":"0","SCITY1":"ICN","SCITY2":"CDG","SDATE1":"2017.06.05.","SDATE2":"2017.06.11.","TRIP":"RT","Where":"mobile"}
#
# headers = {
#     'host': "store.naver.com",
#     'connection': "keep-alive",
#     'accept': "application/json, text/plain, */*",
#     'authorization': "Basic bXlib3R0bGU6d2F0ZXJicm93bg==",
#     'accept-encoding': "gzip, deflate, sdch, br",
#     'accept-language': "ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4",
#     'cache-control': "no-cache",
#     'postman-token': "58973081-9584-a272-bab2-e7e86c3a7a82"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
# data = json.loads(response.content.decode('utf-8'))
# print(data)
# #print(response.text)

# import boto3
#
# arn = 'arn:aws:sns:ap-northeast-1:353716070267:test'
# sns = boto3.client('sns')
#
# sns.publish(
#         TopicArn=arn,
#         Subject=u'타이틀 입니다.',
#         Message='Python Life is short you need Python'
# )
#
#
# from gcm import GCM
#
# gcm = GCM('AIzaSyB2UGIEf-3dVZvtT0CSXzTmrLhGCsMd1XE')
# data = {'message': 'hihihi'}
#
# # Downstream message using JSON request
# reg_ids = ['eQRPiEhsH4w:APA91bHY1BpRKeXMCgS1Vr1CphgIbMvuVezjSIY1WwJf9l2AsFvqcUzV55C9drEVg1eSvBHCA8zwHkpxlP2zG8YG5umpIrFunkclTcJNp6Euzv49iIttwRbBmAAwUNICN9HRSgVazXoy']
# response = gcm.json_request(registration_ids=reg_ids, data=data)
#
# print(response)



import requests
import json, demjson

import re

from pandas import Series, DataFrame
import pandas as pd



# flight
# url = "https://store.naver.com/flights/api/realtime/international"
#
# querystring = {"Adt":"1","Chd":"0","ECITY1":"CDG","ECITY2":"ICN","FareType":"Y","Inf":"0","SCITY1":"ICN","SCITY2":"CDG","SDATE1":"2017.06.05.","SDATE2":"2017.06.11.","TRIP":"RT","Where":"mobile"}
#
# headers = {
#     'host': "store.naver.com",
#     'connection': "keep-alive",
#     'accept': "application/json, text/plain, */*",
#     'authorization': "Basic bXlib3R0bGU6d2F0ZXJicm93bg==",
#     # 'accept-encoding': "gzip, deflate, sdch, br",
#     'accept-language': "ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4",
#     'cache-control': "no-cache"
#     # 'postman-token': "58973081-9584-a272-bab2-e7e86c3a7a82"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# raw_data = json.loads(response.text)
#
# print(response.text)
#
# print(raw_data)


print("------------")
url = "https://kr.hotels.com/search.do?destination=파리&q-check-in=2017-06-06&q-check-out=2017-06-07&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=PRICE"
source_code = requests.get(url, allow_redirects=False)
data = source_code.text

start_pattern = ',\"hotels\":'
start_pattern_index = re.search(start_pattern, data).end()
end_pattern = ',"customerMessaging"'
end_pattern_index = re.search(end_pattern, data).start()

# result = 'start_pattern_index: {}, end_pattern_index: {}, find: {}'.format(start_pattern_index,
#     end_pattern_index,
#     data[start_pattern_index:end_pattern_index]
# )

result = data[start_pattern_index:end_pattern_index]
hotel_result = pd.read_json(result)
print(hotel_result['name'], hotel_result['price'] )

column_names = ['name','hotelid','rank','dealmessage','price','reviewscore','qualityScore']

# open("expedia.txt", 'w', encoding='utf-8').write(data)
# print(data)
