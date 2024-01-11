from pokedex.models import Combat
from random import *

class CombatPokemon:
    def __init__(self, id, pokemonHp1, pokemonHp2, pokemonHp3, pokemonHp4, pokemonHp5, pokemonHp6, pokemonIAHp1,
                 pokemonIAHp2, pokemonIAHp3, pokemonIAHp4, pokemonIAHp5, pokemonIAHp6):
        self.id = id
        self.pokemonHp1 = pokemonHp1,
        self.pokemonHp2 = pokemonHp2,
        self.pokemonHp3 = pokemonHp3,
        self.pokemonHp4 = pokemonHp4,
        self.pokemonHp5 = pokemonHp5,
        self.pokemonHp6 = pokemonHp6,
        self.pokemonIAHp1 = pokemonIAHp1,
        self.pokemonIAHp2 = pokemonIAHp2,
        self.pokemonIAHp3 = pokemonIAHp3,
        self.pokemonIAHp4 = pokemonIAHp4,
        self.pokemonIAHp5 = pokemonIAHp5,
        self.pokemonIAHp6 = pokemonIAHp6,
        self.pokemonIAId1 = randint(1, 151),
        self.pokemonIAId2 = randint(1, 151),
        self.pokemonIAId3 = randint(1, 151),
        self.pokemonIAId4 = randint(1, 151),
        self.pokemonIAId5 = randint(1, 151),
        self.pokemonIAId6 = randint(1, 151)