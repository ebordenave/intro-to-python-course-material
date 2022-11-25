import requests


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


sw_vehicle_search(1, 1, 950000)
