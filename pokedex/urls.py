from django.urls import path

from pokedex import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/<str:string>/<int:number>', views.pokemon, name='pokemon'),
    path('combat/', views.combat, name='combat'),
    path('pokedex/', views.pokedex, name='pokedex'),
    path('update/', views.updateBDD, name='updateBDD')
]
