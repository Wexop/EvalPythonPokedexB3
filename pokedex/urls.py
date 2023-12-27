from django.urls import path

from pokedex import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/<int:id>', views.pokemon, name='pokemon'),
    path('fight/', views.fight, name='fight'),
    path('fight/updateHPAttack', views.updateHPAttack, name='updateHPAttack'),
    path('fight/updateHPAttackSpe', views.updateHPAttackSpe, name='updateHPAttackSpe'),
    path('editTeam/', views.editTeam, name='editTeam'),
    path('fightHome/', views.fightHome, name='fightHome'),
    path('pokedex/', views.pokedex, name='pokedex'),
    path('update/', views.updateBDD, name='updateBDD'),
    path('searchList/', views.searchPokemonList, name='searchList')
]
