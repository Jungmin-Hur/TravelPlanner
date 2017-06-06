import httplib2
import json
import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import uuid

from MainController.models import PriceInfo
from MainController.serializers import PriceInfoSerializer
from MainController.hotelsdotcomclient import get_lowest_price_from_hotels_dot_com
from MainController.naverflightclient import get_lowest_price_from_naver_flight

# from gcm import GCM

class TripService:

    def set_price_info(regs_id, type, querystring):
        price_info_id = uuid.uuid4()
        info = PriceInfo(price_info_id=price_info_id, regs_id=regs_id, type=type, querystring=querystring)

        # lowest_price = int(0)
        # if type == 'F':
        #     # flight_url = "https://store.naver.com/flights/api/realtime/international"
        #     lowest_price = get_lowest_price_from_naver_flight(querystring)
        # elif type == 'H':
        #     lowest_price = get_lowest_price_from_hotels_dot_com(querystring)
        #
        # info.price = lowest_price
        info.save()

        return price_info_id

    def remove_price_info(price_info_id):
        info = PriceInfo.objects.filter(price_info_id=price_info_id)
        # info[0].price_info_id = price_info_id + "DELETED"
        info.delete()
        return "SUCCESS"

    def search_lowest_price():
        info_list = PriceInfo.objects.all()
        # lowest_price_list = list()

        for info in info_list :
            price_info_id = info.price_info_id
            regs_id = info.regs_id
            type = info.type
            price = info.price

            lowest_price = int(0)
            if type == 'F':
                # flight_url = "https://store.naver.com/flights/api/realtime/international"
                # lowest_price = get_lowest_price_from_naver_flight(flight_url, info.headers, info.querystring)
                lowest_price = get_lowest_price_from_naver_flight(info.querystring)
                # lowest_price = get_lowest_price_from_naver_flight(flight_url, json.loads(str.replace(info.headers,"'",'"')), json.loads(str.replace(info.querystring,"'",'"')))
            elif type == 'H':
                lowest_price = get_lowest_price_from_hotels_dot_com(info.querystring)

            # 최저가 발생
            if price == 0 or price > lowest_price:
                #TODO CALL GCM
                # API_KEY = 'AIzaSyA6Px3pCas0Fi8Jlb5-aUNZTFiBmZLqeB4'
                # gcm_return_data = {'data': 'price alarm'}
                # gcm = GCM(API_KEY)
                # reg_id = ''
                # gcm.plaintext_request(registration_id=reg_id, data=gcm_return_data)

                info.price = lowest_price
                info.save()

        return "SUCCESS"

    def get_flight_price_info(price_info_id, page_no):
        info_list = PriceInfo.objects.filter(price_info_id=price_info_id)
        total_count = info_list.__len__();

        #TODO paging results by page_no searching price_info_id
        if total_count > 0 :
            print(info_list[0].flight_data)
            result = info_list[0].flight_data
            return result
        return ''

    def get_hotel_price_info(price_info_id, page_no):
        info_list = PriceInfo.objects.filter(price_info_id=price_info_id)
        total_count = info_list.__len__();

        #TODO paging results by page_no searching price_info_id
        if total_count > 0:
            print(info_list[0].flight_data)
            result = info_list[0].hotel_data
            return result
        return ''


