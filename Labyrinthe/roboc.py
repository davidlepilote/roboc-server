# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

# On charge les cartes existantes
from pickle import Pickler, Unpickler

from Labyrinthe.carte import Carte

def choisir_carte(cartes):
    choix = input("Entrez un numéro de labyrinthe pour commencer à jouer : ")
    choix = int(choix)
    if choix < 1 or choix > len(cartes):
        raise ValueError
    return cartes[choix-1]

def sauvegarder(carte):
    with open('save', 'wb') as fichier:
        pickler = Pickler(fichier)
        pickler.dump(carte)

def charger():
    if os.path.isfile('save'):
        with open('save', 'rb') as fichier:
            unpickler = Unpickler(fichier)
            return unpickler.load()

def supprimer_sauvegarde():
    if os.path.isfile('save'):
        os.remove('save')

def choix_carte():
    global carte
    cartes = []
    for nom_fichier in os.listdir("cartes"):
        if nom_fichier.endswith(".txt"):
            chemin = os.path.join("cartes", nom_fichier)
            nom_carte = nom_fichier[:-3].lower()
            with open(chemin, "r") as fichier:
                contenu = fichier.read()
                cartes.append(Carte(chemin, contenu))
                # Création d'une carte, à compléter

    # On affiche les cartes existantes
    print("Labyrinthes existants :")
    for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))
    print()
    # On choisit la carte
    carte_ok = False
    while not carte_ok:
        try:
            return choisir_carte(cartes)
        except ValueError:
            carte_ok = False

carte = charger()
if carte is not None:
    reponse = ''
    while reponse.upper() not in {'O', 'N'}:
        reponse = input("Voulez vous reprendre la partie sauvegardée ? (O/N)")
    if reponse.upper() == 'N':
        carte = choix_carte()
else:
    carte = choix_carte()

laby = carte.labyrinthe
carte.ajouter_joueur()
carte.ajouter_joueur()

print(carte)
while not laby.gagne():
    try:
        continue_jouer = laby.jouer(input('> '), 0)
        sauvegarder(carte)
        if not continue_jouer:
            break
        print(carte)
    except AssertionError as e:
        print(e)
    except ValueError as e:
        print(e)

if laby.gagne():
    print("Félicitations ! Vous avez gagné !")
    supprimer_sauvegarde()
else:
    print("A bientôt!")
