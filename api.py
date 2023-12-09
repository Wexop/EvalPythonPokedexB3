import requests

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
            pok.toPokemonModel().save()

    def search(self, value: str):
        self.actualPokemonTab = self.pokemons.copy()
        if value != "":
            self.actualPokemonTab = [p for p in self.pokemons.copy() if value in p.name]
        return self.actualPokemonTab

    def getOnePokemon(self, id):
        for i in self.pokemons:
            if i.id == id:
                return i
