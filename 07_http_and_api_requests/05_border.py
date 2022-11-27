import requests
import json


# def borders(country_name_a: str, country_name_b: str) -> bool:
def borders(country_name_a: str, country_name_b: str) -> bool:
    url = 'https://restcountries.com/v3.1/name/'
    a_response = requests.get(url + country_name_a)
    b_response = requests.get(url + country_name_b)

    a_data = a_response.json()
    b_data = b_response.json()

    for item in a_data:
        try:
            print(
                f"country A name with '{country_name_a}' in it => {item['name']['common']} and it borders {item['borders']}")
        except KeyError:
            pass
    print('-' * 150)
    for item in b_data:
        try:
            print(
                f"country B name with '{country_name_b}' in it => {item['name']['common']} and it borders {item['borders']}")
        except KeyError:
            pass


        # print(f"dictionary => {item}")

    # print(data)
    # for item in data:
    #     print(item)


borders('united', 'republic')
