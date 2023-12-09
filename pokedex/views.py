from django.shortcuts import render, redirect
from django.http import *

# Create your views here.
def index(request):
    context = {'list_choice': ['Pokedex', 'Combat']}
    return render(request, 'pokedex/index.html', context)

def combat(request):
    return HttpResponse("<h2>Créer votre deck pour un combat Pokémon</h2>")

def pokemon(request, string, number):
    context = {'string': f'{string}', 'number': f'{number}'}
    return render(request, 'pokedex/pokemon.html', context)

def pokedex(request):
    return redirect(pokemon, "bulbizarre", 1)