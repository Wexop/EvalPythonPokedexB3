from django.contrib import admin

from pokedex.models import Pokemon, Pokemon_team, Combat

admin.site.register(Pokemon)
admin.site.register(Pokemon_team)
admin.site.register(Combat)
