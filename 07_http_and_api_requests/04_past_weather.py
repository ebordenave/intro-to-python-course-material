import requests


# def past_weather(days: int, hours: int, minutes: int, us_zip: str)-> float:
def past_weather(us_zip: str) -> float:
    my_dict = {}
    api_key = 'a24eb87bf52d34ce70b21764f0103579'
    time = 1586468027

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

        if us_zip in my_dict.values():
            print(f"dictionary => {my_dict}")
            lat = my_dict['lat']
            lon = my_dict['lon']
            # print(f"latitude => {lat}, longitude => {lon}")
            url = f'https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={api_key}'
            response = requests.get(url)
            data = response.json()
            print(f"data => {data}")

    # for line in loc_text.split(','):
    #     print(f" => {line}")

    # for zip_code in loc_text:
    #     if zip_code == '00601':
    #         print(zip_code, end='')


past_weather('97910')

# https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API key}
# https://gist.githubusercontent.com/erichurst/7882666/raw/5bdc46db47d9515269ab12ed6fb2850377fd869e/US%2520Zip%2520Codes%2520from%25202013%2520Government%2520Data
