import requests


def borders(country_name_a: str, country_name_b: str) -> bool:
    cca3 = None
    url = 'https://restcountries.com/v3.1/name/'
    a_response = requests.get(url + country_name_a)
    b_response = requests.get(url + country_name_b)

    a_data = a_response.json()
    b_data = b_response.json()

    try:
        for item in a_data:
            try:
                cca3 = item['cca3']
                print(
                    f"country A name with '{country_name_a}' in it => {item['name']['common']} and it borders {item['borders']}")
                # print(f"country A name with '{country_name_a}' cca3 code => {item['cca3']}")
            except KeyError:
                pass
    except KeyError:
        pass

    print('-' * 100)

    try:
        for item in b_data:
            try:
                border_countries = item['borders']
                print(
                    f"country B name with '{country_name_b}' in it => {item['name']['common']} and it borders {item['borders']}")
            except KeyError:
                pass
    except KeyError:
        pass

    try:
        print(cca3)
        if cca3 in border_countries:
            print("do they border? yes")
            return True
        else:
            print("do they border? no")
            return False
    except KeyError:
        print("do they border? no")
        return False

# try combining these into single sets for A and B


borders('saudi', 'qat')
