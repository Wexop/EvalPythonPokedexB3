
from django.http import *
from django.shortcuts import render, redirect
from django.template import loader

from api import Api
from pokedex.models import Pokemon, Pokemon_team, Combat

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
    id = request.GET.get("id")
    id_team = request.GET.get("id_team")
    team = Pokemon_team.objects.get(id=id_team)

    if not id:
        combat = Combat.objects.create()
        id = combat.id

        combat.pokemonHp1 = Pokemon.objects.get(pokemonId=team.pokemon1).hp
        combat.pokemonHp2 = Pokemon.objects.get(pokemonId=team.pokemon2).hp
        combat.pokemonHp3 = Pokemon.objects.get(pokemonId=team.pokemon3).hp
        combat.pokemonHp4 = Pokemon.objects.get(pokemonId=team.pokemon4).hp
        combat.pokemonHp5 = Pokemon.objects.get(pokemonId=team.pokemon5).hp
        combat.pokemonHp6 = Pokemon.objects.get(pokemonId=team.pokemon6).hp

        combat.pokemonIAHp1 = Pokemon.objects.get(pokemonId=combat.pokemonIAId1).hp
        combat.pokemonIAHp2 = Pokemon.objects.get(pokemonId=combat.pokemonIAId2).hp
        combat.pokemonIAHp3 = Pokemon.objects.get(pokemonId=combat.pokemonIAId3).hp
        combat.pokemonIAHp4 = Pokemon.objects.get(pokemonId=combat.pokemonIAId4).hp
        combat.pokemonIAHp5 = Pokemon.objects.get(pokemonId=combat.pokemonIAId5).hp
        combat.pokemonIAHp6 = Pokemon.objects.get(pokemonId=combat.pokemonIAId6).hp

        combat.save()
        return redirect(f"/fight/?id={id}&id_team={id_team}")

    combatExisted = Combat.objects.get(id=id)

    listPokemon = {
        'pokemon1': {
            'pokemon': Pokemon.objects.get(pokemonId=team.pokemon1),
            'hp': combatExisted.pokemonHp1
        },
        'pokemon2': {
            'pokemon': Pokemon.objects.get(pokemonId=team.pokemon2),
            'hp': combatExisted.pokemonHp2
        },
        'pokemon3': {
            'pokemon': Pokemon.objects.get(pokemonId=team.pokemon3),
            'hp': combatExisted.pokemonHp3
        },
        'pokemon4': {
            'pokemon': Pokemon.objects.get(pokemonId=team.pokemon4),
            'hp': combatExisted.pokemonHp4
        },
        'pokemon5': {
            'pokemon': Pokemon.objects.get(pokemonId=team.pokemon5),
            'hp': combatExisted.pokemonHp5
        },
        'pokemon6': {
            'pokemon': Pokemon.objects.get(pokemonId=team.pokemon6),
            'hp': combatExisted.pokemonHp6
        },
    }

    listPokemonIA = {
        'pokemonIA1': {
            'pokemon':Pokemon.objects.get(pokemonId=combatExisted.pokemonIAId1),
            'hp': combatExisted.pokemonIAHp1
        },
        'pokemonIA2': {
            'pokemon': Pokemon.objects.get(pokemonId=combatExisted.pokemonIAId2),
            'hp': combatExisted.pokemonIAHp2
        },
        'pokemonIA3': {
            'pokemon': Pokemon.objects.get(pokemonId=combatExisted.pokemonIAId3),
            'hp': combatExisted.pokemonIAHp3
        },
        'pokemonIA4': {
            'pokemon': Pokemon.objects.get(pokemonId=combatExisted.pokemonIAId4),
            'hp': combatExisted.pokemonIAHp4
        },
        'pokemonIA5': {
            'pokemon': Pokemon.objects.get(pokemonId=combatExisted.pokemonIAId5),
            'hp': combatExisted.pokemonIAHp5
        },
        'pokemonIA6': {
            'pokemon': Pokemon.objects.get(pokemonId=combatExisted.pokemonIAId6),
            'hp': combatExisted.pokemonIAHp6
        }
    }

    context = {'id_team': team.id,
               'id': id,
               'listpokemons': listPokemon,
               'listpokemonsIA': listPokemonIA,
               'selected': 17,
                'selectedIA': 88
               }
    return render(request, "Combat/fight.html", context)

def updateHPAttack(request):
    id = request.GET.get("id")
    id_team = request.GET.get("id_team")
    pokemonId = request.GET.get("pokemon")
    pokemonIAId = request.GET.get("pokemonIa")

    pokemon = Pokemon.objects.get(pokemonId=pokemonId)
    attack = pokemon.attack
    defense = pokemon.defense
    speed = pokemon.speed
    pokemonIA = Pokemon.objects.get(pokemonId=pokemonIAId)
    attackIA = pokemonIA.attack
    defenseIA = pokemonIA.defense
    speedIA = pokemonIA.speed

    combat = Combat.objects.get(id=id)

    while (True):
        if (speed > speedIA):
            if (defenseIA < attack):
                combat.pokemonIAHp1 -= (attack - defenseIA)
            else:
                combat.pokemonIAHp1 -= 1
            if (combat.pokemonIAHp1 <= 0):
                combat.pokemonIAHp1 = 0
                break

            if (defense < attackIA):
                combat.pokemonHp1 -= (attackIA - defense)
            else:
                combat.pokemonHp1 -= 1
            if (combat.pokemonHp1 <= 0):
                combat.pokemonHp1 = 0

        else:
            if (defense < attackIA):
                combat.pokemonHp1 -= (attackIA - defense)
            else:
                combat.pokemonHp1 -= 1
            if (combat.pokemonHp1 <= 0):
                combat.pokemonHp1 = 0
                break

            if (defenseIA < attack):
                combat.pokemonIAHp1 -= (attack - defenseIA)
            else:
                combat.pokemonIAHp1 -= 1
            if (combat.pokemonIAHp1 <= 0):
                combat.pokemonIAHp1 = 0

        break

    combat.save()

    return redirect(f"/fight/?id={id}&id_team={id_team}")

def updateHPAttackSpe(request):
    id = request.GET.get("id")
    id_team = request.GET.get("id_team")
    return redirect(f"/fight/?id={id}&id_team={id_team}")

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