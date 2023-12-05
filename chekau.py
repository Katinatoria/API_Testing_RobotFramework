import requests


def chekai():

    response = requests.get(url="https://rickandmortyapi.com/api/character")

    result = response.json()
    count_char = result['info']['count']
    print(count_char)



search_url_dixie = "https://nominatim.openstreetmap.org/search"


def get_dixie():
    with open("/Addresses", "r", encoding="UTF-8") as f:
        content = list(filter(None, f.read().split('\n')))

    cn = 0
    new_list_add = []

    for i in range(len(content)):
        new_content = content[i].split(',')
        new_list_add.append(new_content)

    print(new_list_add)

    for i in range(len(new_list_add)):
        params_limit = {
            "city": new_list_add[i][0],
            "street": new_list_add[i][1:],
            "format": "json"
        }
        response = requests.get(url=search_url_dixie,
                                params=params_limit)
        result = response.json()
        print(result)


def geocode():
    url = "https://nominatim.openstreetmap.org/search"

    with open("C:/Users/kator/PycharmProjects/HomeWork_Protei_4/Addresses", "r", encoding="UTF-8") as f:
        address = list(filter(None, f.read().split('\n')))

    for i in range(len(address)):
        params = {
            "format": "json",
            "q": address[i]
        }
        response = requests.get(url=search_url_dixie,
                                params=params)
        result = response.json()
        if result:
            return (result[0]["lat"], result[0]["lon"])
        else:
            return None


coordinates = geocode()
print(coordinates)



