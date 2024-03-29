from django.db import models
from random import randint

class Pokemon(models.Model):
    pokemonId = models.IntegerField(default=0)
    name = models.CharField(max_length=255, null=True)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    sprite = models.CharField(max_length=255, null=True)
    type1 = models.CharField(max_length=255, null=True)
    type2 = models.CharField(max_length=255, null=True)
    hp = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    special_attack = models.IntegerField(default=0)
    special_defense = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)

    def create(self, id, name, height, weight, sprite, type1, type2, hp, attack, defense, special_attack,
               special_defense, speed):
        self.pokemonId = id
        self.name = name
        self.height = height / 10
        self.weight = weight / 10
        self.sprite = sprite
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    def getTypeColor(self, type):
        if type == "fire":
            return "#be4f00"
        elif type == "flying":
            return "#BABABAFF"
        elif type == "water":
            return "#0000FF"
        elif type == "bug":
            return "#00C722FF"
        elif type == "poison":
            return "#7D00BAFF"
        elif type == "normal":
            return "#D7D7D7FF"
        elif type == "electric":
            return "#CED500FF"
        elif type == "ground":
            return "#AB8200FF"
        elif type == "fairy":
            return "#F466FFFF"
        elif type == "grass":
            return "#26A200FF"
        elif type == "fighting":
            return "#894900FF"
        elif type == "psychic":
            return "#EB40FFFF"
        elif type == "rock":
            return "#5B5B5BFF"
        elif type == "steel":
            return "#BABABAFF"
        elif type == "ice":
            return "#54F9FFFF"
        elif type == "ghost":
            return "#4500A4FF"
        elif type == "dragon":
            return "#004FE8FF"


class Pokemon_team(models.Model):
    pokemon1 = models.IntegerField(default=1)
    pokemon2 = models.IntegerField(default=1)
    pokemon3 = models.IntegerField(default=1)
    pokemon4 = models.IntegerField(default=1)
    pokemon5 = models.IntegerField(default=1)
    pokemon6 = models.IntegerField(default=1)

class Combat(models.Model):
    pokemonHp1 = models.IntegerField(default=0)
    pokemonHp2 = models.IntegerField(default=0)
    pokemonHp3 = models.IntegerField(default=0)
    pokemonHp4 = models.IntegerField(default=0)
    pokemonHp5 = models.IntegerField(default=0)
    pokemonHp6 = models.IntegerField(default=0)

    pokemonIAHp1 = models.IntegerField(default=0)
    pokemonIAHp2 = models.IntegerField(default=0)
    pokemonIAHp3 = models.IntegerField(default=0)
    pokemonIAHp4 = models.IntegerField(default=0)
    pokemonIAHp5 = models.IntegerField(default=0)
    pokemonIAHp6 = models.IntegerField(default=0)

    pokemonIAId1 = models.IntegerField(default=randint(1, 151))
    pokemonIAId2 = models.IntegerField(default=randint(1, 151))
    pokemonIAId3 = models.IntegerField(default=randint(1, 151))
    pokemonIAId4 = models.IntegerField(default=randint(1, 151))
    pokemonIAId5 = models.IntegerField(default=randint(1, 151))
    pokemonIAId6 = models.IntegerField(default=randint(1, 151))
