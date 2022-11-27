import requests
import json


# def borders(country_name_a: str, country_name_b: str) -> bool:
def borders(country_name_a: str) -> bool:
    url = 'https://restcountries.com/v3.1/name/'
    response = requests.get(url + country_name_a)
    data = response.json()
    print(data)


borders('united')
