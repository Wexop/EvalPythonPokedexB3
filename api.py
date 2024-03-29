import requests

from pokedex.models import Pokemon, Combat, Pokemon_team
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
                            pokemonInfo['sprites'], pokemonInfo['types'], pokemonInfo['stats'])
        tab.append(pok)

    return tab


class Api:

    def __init__(self):
        self.actualPokemonTab = None
        self.pokemons = None
        self.fight = None

    def updateBDD(self):
        self.pokemons = getAllPokemonObject()
        self.actualPokemonTab = self.pokemons.copy()
        Pokemon.objects.all().delete()  # delete all to save it after

        for pok in self.pokemons:
            pok.toPokemonModel().save()
