from django.http import *
from django.shortcuts import render, redirect
from django.template import loader

from api import Api
from pokedex.models import Pokemon


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


def pokemon(request, id):
    idSupp = id+1
    idInf = id-1
    if (idSupp == 152):
        idSupp = 1
    if (idInf == 0):
        idInf = 151
    context = {'pokemon': Pokemon.objects.get(pokemonId=id), 'idSupp':idSupp, 'idInf':idInf}
    return render(request, 'pokedex/pokemon.html', context)


def pokedex(request):
    pokemons = Pokemon.objects.all().values()
    template = loader.get_template('pokedex/list_pokemon.html')
    context = {
        'pokemons': pokemons,
    }
    return HttpResponse(template.render(context, request))


def searchPokemonList(request):
    name = request.GET.get("name")
    pokemons = Pokemon.objects.filter(name__contains=name)
    template = loader.get_template("pokedex/list_pokemon.html")
    context = {
        'pokemons': pokemons
    }

    return HttpResponse(template.render(context, request))
