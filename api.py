import requests

from pokedex.models import Pokemon
from pokemon import PokemonObject

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
        pok = PokemonObject(pokemonInfo['id'], pokemonInfo['name'], pokemonInfo['height'], pokemonInfo['weight'],
                            pokemonInfo['sprites'], pokemonInfo['types'])
        tab.append(pok)

    return tab


class Api:

    def __init__(self):
        self.actualPokemonTab = None
        self.pokemons = None

    def updateBDD(self):
        self.pokemons = getAllPokemonObject()
        self.actualPokemonTab = self.pokemons.copy()

        for pok in self.pokemons:
            pokBDD = Pokemon.objects.get(pokemonId=pok.id)
            if not pokBDD:
                pok.toPokemonModel().save()
