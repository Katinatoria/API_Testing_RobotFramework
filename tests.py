import requests


all_char_url = "https://rickandmortyapi.com/api/character"

def get_all_char():

    response = requests.get(url=all_char_url)

    result = response.json()
    count_char = result['info']['count']
    return count_char


def geocode():
    url = "https://nominatim.openstreetmap.org/search"
    result_list = []
    with open("C:/Users/kator/PycharmProjects/HomeWork_Protei_4/Addresses", "r", encoding="UTF-8") as f:
        address = list(filter(None, f.read().split('\n')))

    for i in range(len(address)):
        params = {
            "format": "json",
            "q": address[i]
        }
        response = requests.get(url=url,
                                params=params)
        result = response.json()
        if result:
            result_list.append(result[0]["lat"])
            result_list.append(result[0]["lon"])
            return result_list
        else:
            return None


def geocode_rev():
    url_2 = "https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>"

    with open("C:/Users/kator/PycharmProjects/HomeWork_Protei_4/Addresses_reverse", "r", encoding="UTF-8") as f:
        coordinates = list(filter(None, f.read().split('\n')))

    for i in range(len(coordinates)):
        params = {
            "format": "json",
            "lat": coordinates[i][0],
            "lon": coordinates[i][1]
        }

        response = requests.get(url=url_2,
                                params=params)
        result = response.json()
        addr_city = result['address']['city']
        if result:
            print(addr_city)
            return addr_city
        else:
            return None


geocode_rev()




