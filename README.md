# Setup

Pour l'installation de ce projet, il faut ouvrir le projet sur un IDE (Pycharm ou autre) et taper les commandes suivantes : 

``` python
py manage.py migrate
```

``` python
py manage.py sqlmigrate pokedex 0008
```

##### Run 

``` python
py manage.py run server
```

# Choix 

Ce projet à été réaliser en python avec le framework Django car le langage étais imposé et que le framework est plus puissant que la librarie Tkinter.
Le choix du "Dark mode" pour l'application est un choix des developpeurs.
# Partie Pokedex

## Première utilisation

Lors de la première utilisation, il faut attendre le chargement des pokemons, ensuite en cliquant sur le bouton "Pokedex", on accède à une page affichant une liste de pokemon (de 1 à 151)

![Homepage](https://github.com/Wexop/EvalPythonPokedexB3/blob/master/AssetsDocs/Pasted%20image%2020231220161617.png?raw=true)

*Page d'accueil*

Le boutons "Update" sert à actualiser les Pokémon dans la base de donnée.

![PokemonList](AssetsDocs/Pasted image 20231220161617.png?raw=true)
*Liste des Pokémons*

Pour avoir plus d'informations il suffit de cliquer sur le bouton "En Savoir plus" affichant ainsi plus d'informations sur le Pokémon :

![Pikaaaaa](AssetsDocs/Pasted image 20231220161918.png?raw=true)
*Page de Pikachu*
# Partie Combat

### Gestion des équipes 

La gestion des équipes se fait via la page "Combat" accessible depuis la page d'accueil

![GestionEquipe2](AssetsDocs/Pasted image 20240111085827.png?raw=true)
*Page de Gestions des Equipes*

![GestionEquipe2](AssetsDocs/Pasted image 20240111084616.png?raw=true)
*Page de Gestions des Equipes*

Une équipe peux sois être "Choisie" pour combattre, "Modifiée" ou "Supprimée".

### Création d'une équipe

![CréaEquipe](AssetsDocs/Pasted image 20240111084842.png?raw=true)
*Page de création d'une équipe*

Pour modifier le Pokémon cliqué dessus et sélectionner le Pokémon par lequel vous souhaités le remplacer.
On peux aussi utiliser une barre de recherche pour trouver le Pokémon adapté.

