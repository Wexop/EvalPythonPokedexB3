from django.http import *
from django.shortcuts import render, redirect

from api import Api


# Create your views here.
def index(request):
    context = {'list_choice': ['Pokedex', 'Combat', "Update"]}
    return render(request, 'pokedex/index.html', context)


def updateBDD(request):
    api = Api()
    api.updateBDD()
    return redirect("/")


def combat(request):
    return HttpResponse("<h2>Créer votre deck pour un combat Pokémon</h2>")


def pokemon(request, string, number):
    context = {'string': f'{string}', 'number': f'{number}'}
    return render(request, 'pokedex/pokemon.html', context)


def pokedex(request):
    return redirect(pokemon, "bulbizarre", 1)
