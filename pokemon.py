from pokedex.models import Pokemon


class PokemonObject:
    def __init__(self, id, name, height, weight, sprites, types):
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight
        self.sprites = sprites
        self.types = types

    def getSpriteUrl(self):
        return self.sprites['other']['official-artwork']['front_default']

    def getTypesStringTab(self):
        tab = []
        for i in self.types:
            tab.append(i['type']['name'])

        return tab

    def toPokemonModel(self):
        type2 = "aucun"
        if (len(self.getTypesStringTab()) == 2):
            type2 = self.getTypesStringTab()[1]
        pokemon = Pokemon()
        pokemon.create(self.id, self.name, self.height, self.weight, self.getSpriteUrl(),
                       self.getTypesStringTab()[0], type2)
        return pokemon
