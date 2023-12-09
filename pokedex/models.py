from django.db import models


class Pokemon(models.Model):
    pokemonId = models.IntegerField(default=0)
    name = models.CharField(max_length=255, null=True)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    sprite = models.CharField(max_length=255, null=True)
    type1 = models.CharField(max_length=255, null=True)
    type2 = models.CharField(max_length=255, null=True)

    def create(self, id, name, height, weight, sprite, type1, type2):
        self.pokemonId = id
        self.name = name
        self.height = height
        self.weight = weight
        self.sprite = sprite
        self.type1 = type1
        self.type2 = type2
