import requests
import re
import pandas as pd
from pandas import Series, DataFrame

def get_lowest_price_from_hotels_dot_com(querystring):
    source_code = requests.get(querystring, allow_redirects=False)
    data = source_code.text

    start_pattern = ',\"hotels\":'
    start_pattern_index = re.search(start_pattern, data).end()
    end_pattern = ',"customerMessaging"'
    end_pattern_index = re.search(end_pattern, data).start()

    result = data[start_pattern_index:end_pattern_index]
    hotel_result = pd.read_json(result)
    lowest_price = int(hotel_result['price'][0])

    for price in hotel_result['price']:
        # print(str(lowest_price) + ' : ' + str(price))
        if lowest_price > int(price):
            lowest_price = int(price)
    return lowest_price

# price = get_lowest_price_from_hotels_dot_com("https://kr.hotels.com/search.do?destination=파리&q-check-in=2017-06-06&q-check-out=2017-06-07&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=PRICE")
# print(price)
