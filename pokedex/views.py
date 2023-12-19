from django.http import *
from django.shortcuts import render, redirect
from django.template import loader

from api import Api
from pokedex.models import Pokemon

api = Api()


# Create your views here.
def index(request):
    pokemons = Pokemon.objects.all()
    context = {'list_choice': ['Pokedex', 'FightHome', "Update"], "updating": len(pokemons) == 0}
    return render(request, 'pokedex/index.html', context)


def updateBDD(request):
    api = Api()
    api.updateBDD()
    return redirect("/")


def fightHome(request):
    return render(request, "Combat/teamChoice.html")

def fight(request):
    return render(request, "Combat/fight.html")

def editTeam(request):
    return render(request, "Combat/teamEdit.html")



def pokemon(request, id):
    idSupp = id + 1
    idInf = id - 1
    if (idSupp == 152):
        idSupp = 1
    if (idInf == 0):
        idInf = 151
    pok = Pokemon.objects.get(pokemonId=id)
    context = {'pokemon': pok,
               'idSupp': idSupp,
               'idInf': idInf,
               "colorType1": pok.getTypeColor(pok.type1),
               "colorType2": pok.getTypeColor(pok.type2)
               }
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
