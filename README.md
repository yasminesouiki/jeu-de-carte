# Jeu de Cartes Mémoire

## Description
Ce projet est un jeu de mémoire simple développé en Python en utilisant la bibliothèque Tkinter pour l'interface utilisateur. Le jeu consiste à retourner des cartes et à essayer de trouver toutes les paires correspondantes.

## Fonctionnalités
- **Cartes aléatoires :** Les icônes des cartes sont mélangées aléatoirement à chaque partie.
- **Interface graphique :** Une interface utilisateur simple et intuitive avec des boutons de cartes.
- **Rejouer :** Un bouton pour redémarrer le jeu avec un nouvel arrangement aléatoire des cartes.
- **Quitter :** Un bouton pour fermer le jeu.

## Icônes de cartes
Les cartes utilisent les icônes suivantes : 🍎, 🍉, 🌸, ✨, 🍒, ❤️, 🍕, ⚽️. Chaque icône apparaît deux fois.

## Prérequis
- Python 3.x
- Tkinter (inclus dans la plupart des distributions Python)

## Installation
Clonez ce dépôt sur votre machine locale :
```bash
git clone https://github.com/votre-utilisateur/jeu-de-cartes-memoire.git
cd jeu-de-cartes-memoire
```

## Utilisation
Exécutez le script Python pour démarrer le jeu :
```bash
python jeu_de_cartes_memoire.py
```

## Explication du Code
- **Importation des modules :** Le code importe les modules `tkinter`, `random` et `time`.
- **Liste des icônes de cartes :** Les icônes des cartes sont stockées dans une liste et mélangées aléatoirement.
- **Fenêtre principale :** La fenêtre principale de l'application est créée.
- **Fonction `card_click` :** Cette fonction gère la logique de retournement des cartes et de vérification des paires correspondantes.
- **Fonction `rejouer` :** Cette fonction permet de redémarrer le jeu.
- **Fonction `quitter` :** Cette fonction permet de fermer l'application.
- **Création et placement des boutons de cartes :** Les boutons de cartes sont créés et placés dans une grille.
- **Boutons supplémentaires :** Deux boutons supplémentaires sont ajoutés pour rejouer et quitter le jeu.

## Auteur
Ce projet a été développé par Yasmine Souiki.
