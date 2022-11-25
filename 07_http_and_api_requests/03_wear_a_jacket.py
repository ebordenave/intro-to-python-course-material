import requests


def wear_a_jacket(us_zip: str) -> bool:
    url = (
        f'https://api.openweathermap.org/data/2.5/weather?zip={us_zip}&appid=a24eb87bf52d34ce70b21764f0103579&units=imperial')
    response = requests.get(url)
    data = response.json()

    weather = data['weather']
    main = data['main']
    # print(main)
    # print(weather)

    new_ls = next((item for item in weather if item['main'] != 'rain' and item['main'] != 'snow'), None)

    if not new_ls:
        # print("wear a jacket its raining or snowing")
        return True
    elif new_ls:
        for keys, values in main.items():
            if keys == 'feels_like' and values < float(60.00):
                # print("wear a jacket its cold")
                return True
            else:
                # print("no jacket needed")
                return False


wear_a_jacket('33101')
