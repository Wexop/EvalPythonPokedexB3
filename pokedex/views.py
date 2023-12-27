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
            'pokemon': Pokemon.objects.get(pokemonId=combatExisted.pokemonIAId1),
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

    selectedPokemon = {
        'pokemon': Pokemon.objects.get(pokemonId=team.pokemon1),
        'selection': team.pokemon1
    }
    selectedPokemonIA = {
        'pokemon': Pokemon.objects.get(pokemonId=combatExisted.pokemonIAId1),
        'selection': combatExisted.pokemonIAId1
    }

    if combatExisted.pokemonHp1 <= 0:
        selectedPokemon = {
        'pokemon': Pokemon.objects.get(pokemonId=team.pokemon2),
        'selection': team.pokemon2
    }
    elif combatExisted.pokemonHp2 <= 0:
        selectedPokemon = {
        'pokemon': Pokemon.objects.get(pokemonId=team.pokemon3),
        'selection': team.pokemon3
    }
    elif combatExisted.pokemonHp3 <= 0:
        selectedPokemon = {
        'pokemon': Pokemon.objects.get(pokemonId=team.pokemon4),
        'selection': team.pokemon4
    }
    elif combatExisted.pokemonHp4 <= 0:
        selectedPokemon = {
        'pokemon': Pokemon.objects.get(pokemonId=team.pokemon5),
        'selection': team.pokemon5
    }
    elif combatExisted.pokemonHp5 <= 0:
        selectedPokemon = {
        'pokemon': Pokemon.objects.get(pokemonId=team.pokemon6),
        'selection': team.pokemon6
    }

    if combatExisted.pokemonIAHp1 <= 0:
        selectedPokemon = {
        'pokemon': Pokemon.objects.get(pokemonId=combatExisted.pokemonIAId2),
        'selection': combatExisted.pokemonIAId2
    }
    elif combatExisted.pokemonIAHp2 <= 0:
        selectedPokemon = {
        'pokemon': Pokemon.objects.get(pokemonId=combatExisted.pokemonIAId3),
        'selection': combatExisted.pokemonIAId3
    }
    elif combatExisted.pokemonIAHp3 <= 0:
        selectedPokemon = {
        'pokemon': Pokemon.objects.get(pokemonId=combatExisted.pokemonIAId4),
        'selection': combatExisted.pokemonIAId4
    }
    elif combatExisted.pokemonIAHp4 <= 0:
        selectedPokemon = {
        'pokemon': Pokemon.objects.get(pokemonId=combatExisted.pokemonIAId5),
        'selection': combatExisted.pokemonIAId5
    }
    elif combatExisted.pokemonIAHp5 <= 0:
        selectedPokemon = {
        'pokemon': Pokemon.objects.get(pokemonId=combatExisted.pokemonIAId6),
        'selection': combatExisted.pokemonIAId6
    }

    context = {'id_team': team.id,
               'id': id,
               'listpokemons': listPokemon,
               'listpokemonsIA': listPokemonIA,
               'selected': selectedPokemon,
               'selectedIA': selectedPokemonIA
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

    team = Pokemon_team.objects.get(id=id_team)

    HP = 0
    HPIA = 0

    if pokemonId == team.pokemon1:
        HP = combat.pokemonHp1
    elif pokemonId == team.pokemon2:
        HP = combat.pokemonHp2
    elif pokemonId == team.pokemon3:
        HP = combat.pokemonHp3
    elif pokemonId == team.pokemon4:
        HP = combat.pokemonHp4
    elif pokemonId == team.pokemon5:
        HP = combat.pokemonHp5
    elif pokemonId == team.pokemon6:
        HP = combat.pokemonHp6

    if pokemonIAId == combat.pokemonIAId1:
        HPIA = combat.pokemonIAHp1
    if pokemonIAId == combat.pokemonIAId2:
        HPIA = combat.pokemonIAHp2
    elif pokemonIAId == combat.pokemonIAId3:
        HPIA = combat.pokemonIAHp3
    elif pokemonIAId == combat.pokemonIAId4:
        HPIA = combat.pokemonIAHp4
    elif pokemonIAId == combat.pokemonIAId5:
        HPIA = combat.pokemonIAHp5
    elif pokemonIAId == combat.pokemonIAId6:
        HPIA = combat.pokemonIAHp6

    atckIndicator = True

    while atckIndicator:
        if speed > speedIA:
            if defenseIA < attack:
                HPIA -= (attack - defenseIA)
            else:
                HPIA -= 1
            if HPIA <= 0:
                HPIA = 0
                break

            if defense < attackIA:
                HP -= (attackIA - defense)
            else:
                HP -= 1
            if HP <= 0:
                HP = 0
        else:
            if defense < attackIA:
                HP -= (attackIA - defense)
            else:
                HP -= 1
            if HP <= 0:
                HP = 0
                break

            if defenseIA < attack:
                HPIA -= (attack - defenseIA)
            else:
                HPIA -= 1
            if HPIA <= 0:
                HPIA = 0

        atckIndicator = False

    if pokemonId == team.pokemon1:
        combat.pokemonHp1 = HP
    elif pokemonId == team.pokemon2:
        combat.pokemonHp2 = HP
    elif pokemonId == team.pokemon3:
        combat.pokemonHp3 = HP
    elif pokemonId == team.pokemon4:
        combat.pokemonHp4 = HP
    elif pokemonId == team.pokemon5:
        combat.pokemonHp5 = HP
    elif pokemonId == team.pokemon6:
        combat.pokemonHp6 = HP

    if pokemonIAId == combat.pokemonIAId1:
        combat.pokemonIAHp1 = HPIA
    elif pokemonIAId == combat.pokemonIAId2:
        combat.pokemonIAHp2 = HPIA
    elif pokemonIAId == combat.pokemonIAId3:
        combat.pokemonIAHp3 = HPIA
    elif pokemonIAId == combat.pokemonIAId4:
        combat.pokemonIAHp4 = HPIA
    elif pokemonIAId == combat.pokemonIAId5:
        combat.pokemonIAHp5 = HPIA
    elif pokemonIAId == combat.pokemonIAId6:
        combat.pokemonIAHp6 = HPIA

    combat.save()

    context = {
        'hp': HP,
        'hpia': HPIA,
        'HP': combat.pokemonHp1,
        'HPIA':combat.pokemonIAHp1,
    }
    return render(request, "Combat/test.html", context)
    # return redirect(f"/fight/?id={id}&id_team={id_team}")


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
