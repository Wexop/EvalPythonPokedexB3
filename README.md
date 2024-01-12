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

![Homepage](https://github.com/Wexop/EvalPythonPokedexB3/blob/master/AssetsDocs/Pasted%20image%2020231220161655.png?raw=true)
*Page d'accueil*

Le boutons "Update" sert à actualiser les Pokémon dans la base de donnée.

![PokemonList](https://github.com/Wexop/EvalPythonPokedexB3/blob/master/AssetsDocs/Pasted%20image%2020231220161617.png?raw=true)
*Liste des Pokémons*

Pour avoir plus d'informations il suffit de cliquer sur le bouton "En Savoir plus" affichant ainsi plus d'informations sur le Pokémon :

![Pikaaaaa](https://github.com/Wexop/EvalPythonPokedexB3/blob/master/AssetsDocs/Pasted%20image%2020231220161918.png?raw=true)
*Page de Pikachu*
# Partie Combat

### Gestion des équipes 

La gestion des équipes se fait via la page "Combat" accessible depuis la page d'accueil

![GestionEquipe2](https://github.com/Wexop/EvalPythonPokedexB3/blob/master/AssetsDocs/Pasted%20image%2020240111085827.png?raw=true)
*Page de Gestions des Equipes*

![GestionEquipe2](https://github.com/Wexop/EvalPythonPokedexB3/blob/master/AssetsDocs/Pasted%20image%2020240111084616.png?raw=true)
*Page de Gestions des Equipes*

Une équipe peux sois être "Choisie" pour combattre, "Modifiée" ou "Supprimée".

### Création d'une équipe

![CréaEquipe](https://github.com/Wexop/EvalPythonPokedexB3/blob/master/AssetsDocs/Pasted%20image%2020240111084842.png?raw=true)
*Page de création d'une équipe*

Pour modifier le Pokémon cliqué dessus et sélectionner le Pokémon par lequel vous souhaités le remplacer.
On peux aussi utiliser une barre de recherche pour trouver le Pokémon adapté.

### Lancement d'un combat
*Avant tout, la partie combat n'a pas pu être terminée complétement. Nous avons tout de même fait quelques tests que nous expliquerons dans cette partie*

#### Choisir son équipe
![ChoixEquipe](https://github.com/Wexop/EvalPythonPokedexB3/blob/master/AssetsDocs/choose_team.png?raw=true)

Avant de pouvoir lancer un combat, il faut d'abord sélectionner l'équipe que nous voulons faire combattre contre l'ordinateur.

De base l'équipe sélectionnée sera la première équipe enregistré mais il est possible de choisir l'équipe que l'on souhaite en cliquant sur le bouton choisir à côté de l'équipe.

L'équipe sélectionnée est celle qui est entouré d'un liseré bleu.

![ImpossibleSansEquipe](https://github.com/Wexop/EvalPythonPokedexB3/blob/master/AssetsDocs/zero_team.png?raw=true)

**On ne peut lancer un combat seulement si une équipe a déjà été créée auparavant.**

Pour lancer le combat il suffira de cliquer sur le bouton rouge "COMBATTRE" après avoir sélectionné son équipe.

#### Le combat

![Combat](https://github.com/Wexop/EvalPythonPokedexB3/blob/master/AssetsDocs/combat.png?raw=true)

Arrivé sur cette page, l'équipe de l'ordinateur est générée automatiquement et est liée à l'id du combat donc si on quitte le combat en faisant un retour à l'accueil, il sera impossible de revenir sur cette partie car l'id du combat se génère lorsqu'on clique sur le bouton "COMBATTRE" vu précèdemment.

A gauche et à droite nous avons les deux équipes de Pokémon affichées avec le sprite et les points de vie de chaque pokémon.

Au milieu nous avons le premier duel (votre pokémon est celui qui est le plus proche des boutons d'action).

**Deux actions sont disponibles : l'attaque et l'attaque spéciale**

Si on choisit "Attaque", les deux pokémons vont s'affronter sur leurs statistiques d'attaque et de défense, et c'est le plus rapide des deux qui attaquent en premier.

C'est la même logique pour l'"Attaque spéciale" mais avec les statistiques d'attaque spéciale et de défense spéciale.

*L'application fonctionne jusqu'à ce qu'un premier pokémon tombe K.O.*

# Repos Github

Le repos reste disponible sur Github à l'adresse suivante : 
https://github.com/Wexop/EvalPythonPokedexB3