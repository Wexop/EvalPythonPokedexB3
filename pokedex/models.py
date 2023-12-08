from django.db import models


class Pokemon:
    def __init__(self, id, name, height, weight, sprite, type1, type2):
        self.id = models.IntegerField(id)
        self.name = models.CharField(name)
        self.height = models.IntegerField(height)
        self.weight = models.IntegerField(weight)
        self.sprite = models.CharField(sprite)
        self.type1 = models.CharField(type1)
        self.type2 = models.CharField(type2)
