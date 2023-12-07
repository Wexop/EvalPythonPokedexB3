class Pokemon:
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
