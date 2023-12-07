import requests

from pokemon import Pokemon

ALL_POKEMON_URL = "https://pokeapi.co/api/v2/pokemon?limit=151"
POKEMON_INFO_URL = "https://pokeapi.co/api/v2/pokemon/:id/"
POKEMON_TYPE_URL = "https://pokeapi.co/api/v2/type/:id/"


def getUrlPokemonInfo(id):
    return POKEMON_INFO_URL.replace(":id", id)


def getUrlTypeInfo(id):
    return POKEMON_TYPE_URL.replace(":id", id)


def getAllPokemonObject():
    res = requests.get(ALL_POKEMON_URL).json()
    tab = []
    for i in res['results']:
        pokemonInfo = requests.get(i['url']).json()
        pok = Pokemon(pokemonInfo['id'], pokemonInfo['name'], pokemonInfo['height'], pokemonInfo['weight'],
                      pokemonInfo['sprites'], pokemonInfo['types'])
        tab.append(pok)

    return tab


print(getAllPokemonObject())
