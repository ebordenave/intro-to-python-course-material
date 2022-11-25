import requests


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


starship_piloted_species('Millennium Falcon')
