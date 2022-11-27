import requests
import time


def past_weather(days: int, hours: int, minutes: int, us_zip: str) -> float:
    seconds = (60 * minutes) + (hours * 3600) + (24 * 3600 * days)
    past_time = int(time.time() - seconds)
    my_dict = {}
    api_key = 'a24eb87bf52d34ce70b21764f0103579'

    # this block below retrieves all longitude and latitude values from repo
    # results are dictionaries of longitude and latitude
    loc_url = 'https://gist.githubusercontent.com/erichurst/7882666/raw/5bdc46db47d9515269ab12ed6fb2850377fd869e/US%2520Zip%2520Codes%2520from%25202013%2520Government%2520Data'
    loc_response = requests.get(loc_url)
    loc_text = loc_response.text.split('\n')
    for text in loc_text:
        text = text.split(',')
        for elem in text:
            if len(elem) == 5:
                my_dict['zip_code'] = elem
            elif len(elem) == 9:
                my_dict['lat'] = float(elem.strip())
            elif len(elem) > 9:
                my_dict['lon'] = float(elem.strip())

        # this block filters dictionaries using us_zip_code value inputted from user
        # assigns values to lat and lon variables
        if us_zip in my_dict.values():
            # print(f"dictionary => {my_dict}")
            lat = my_dict['lat']
            lon = my_dict['lon']
            # print(f"latitude => {lat}, longitude => {lon}")
            params = {'lat': lat, 'lon': lon, 'dt': past_time, 'units': 'imperial', 'appid': api_key}
            url = 'https://api.openweathermap.org/data/3.0/onecall/timemachine'
            response = requests.get(url, params=params)
            data = response.json()

            # last step is to return temperature at past_time
            for k, v in data.items():
                if k == 'data':
                    my_list = [item['temp'] for item in v]
                    for item in my_list:
                        temp = item
                        print(temp)
                        return temp


past_weather(0, 20, 54, '02186')
