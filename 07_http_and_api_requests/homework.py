import requests
import time


def sw_vehicle_search(cargo_capacity: int, max_speed: int, cost: int) -> list:
    all_vehicles = []
    query_matches = []
    url = 'https://swapi.dev/api/vehicles/'
    response = requests.get(url)
    data = response.json()

    # store the first page of results
    all_vehicles = all_vehicles + data['results']

    while data['next'] is not None:
        print("Next page found, downloading", data['next'])
        response = requests.get(data['next'])
        data = response.json()
        all_vehicles = all_vehicles + data['results']

    for vehicles in all_vehicles:
        try:
            if int(vehicles['cargo_capacity']) >= cargo_capacity and int(
                    vehicles['max_atmosphering_speed']) >= max_speed and int(vehicles['cost_in_credits']) <= cost:
                query_matches.append(vehicles['name'])
        except ValueError:
            pass
    # print(f"vehicles that match query => {query_matches}")
    return query_matches


def starship_piloted_species(starship: str) -> list:
    total_starships = []
    query_matches = []
    url = 'https://swapi.dev/api/starships/'
    response = requests.get(url)
    data = response.json()

    total_starships = total_starships + data['results']

    while data['next'] is not None:
        print("Next page found, downloading", data['next'])
        response = requests.get(data['next'])
        data = response.json()
        total_starships = total_starships + data['results']

    for ship in total_starships:
        if ship['name'] == starship:
            for pilot_url in ship['pilots']:
                pilot_response = requests.get(pilot_url)
                pilot_data = pilot_response.json()
                # print(pilot_data['species'])
                if not pilot_data['species']:
                    pilot_data['species'] = 'Human'
                    query_matches.append(pilot_data['species'])
                else:
                    for species_url in pilot_data['species']:
                        species_response = requests.get(species_url)
                        species_data = species_response.json()
                        species = species_data['name']
                        query_matches.append(species)
                        # print(species)
    print(query_matches)
    return query_matches


def wear_a_jacket(us_zip: str) -> bool:
    url = (
        f'https://api.openweathermap.org/data/2.5/weather?zip={us_zip}&appid=a24eb87bf52d34ce70b21764f0103579&units=imperial')
    response = requests.get(url)
    data = response.json()

    weather = data['weather']
    main = data['main']
    print(f"main => {main}")
    print(f"weather => {weather}")

    new_ls = next((item for item in weather if item['main'] != 'Rain' and item['main'] != 'Snow'), None)

    if not new_ls:
        print("wear a jacket its raining or snowing")
        return True

    if main['feels_like'] <= float(60.00):
        print("wear a jacket its cold")
        return True
    else:
        print("no jacket needed")
        return False


def past_weather(days: int, hours: int, minutes: int, us_zip: str) -> float:
    past_time = int(time.time() - (days * hours * minutes * 60))
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
            print(f"dictionary => {my_dict}")
            lat = my_dict['lat']
            lon = my_dict['lon']
            # print(f"latitude => {lat}, longitude => {lon}")
            params = {'lat': lat, 'lon': lon, 'dt': past_time, 'units': 'imperial', 'appid': api_key}
            url = 'https://api.openweathermap.org/data/3.0/onecall/timemachine'
            response = requests.get(url, params=params)
            data = response.json()
            print(f"data => {data}")

            # last step is to return temperature at past_time
            for k, v in data.items():
                if k == 'data':
                    new_dict = next((item for item in v if item['temp'] != 'Rain' and item['temp'] != 'Snow'), None)
                    temp = new_dict['temp']
                    print(temp)
                    return temp


past_weather(4, 0, 5, '02186')
