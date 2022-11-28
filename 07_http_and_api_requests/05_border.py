import requests
import json


# def borders(country_name_a: str, country_name_b: str) -> bool:
def borders(country_name_a: str, country_name_b: str) -> bool:
    cca3 = None
    url = 'https://restcountries.com/v3.1/name/'
    a_response = requests.get(url + country_name_a)
    b_response = requests.get(url + country_name_b)

    a_data = a_response.json()
    b_data = b_response.json()

    for item in a_data:
        try:
            print(
                f"country A name with '{country_name_a}' in it => {item['name']['common']} and it borders {item['borders']}")
            # print(f"country A name with '{country_name_a}' cca3 code => {item['cca3']}")

        except KeyError:
            pass
        cca3 = item['cca3']
        print(f"country code for {item['name']['common']} is {cca3}")

    print('-' * 100)

    for item in b_data:
        try:
            print(
                f"country B name with '{country_name_b}' in it => {item['name']['common']} and it borders {item['borders']}")
        except KeyError:
            pass

        try:
            border_countries_b = item['borders']
            if cca3 in border_countries_b:
                print("do they border? yes")
                return True
            else:
                print("do they border? no")
                return False
        except KeyError:
            print("do they border? no")
            return False

        # print(f"dictionary => {item}")

    # print(data)
    # for item in data:
    #     print(item)


# get cca3 of country a and country b
# get dictionary of bordering countries for both country a and country b
# check dictionary if cca3 of country a exists in dictionary

borders('haiti', 'dominican')
