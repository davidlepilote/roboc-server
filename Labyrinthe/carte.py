# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
import random

from Labyrinthe.labyrinthe import Labyrinthe


def creer_labyrinthe_depuis_chaine(chaine):
    labyrinthe = Labyrinthe()
    ligne = 0
    colonne = 0
    for case in chaine:
        if case == "\n":
            ligne += 1
            labyrinthe.nb_colonnes = colonne
            colonne = 0
            continue
        if case == "O":
            labyrinthe.grille[Labyrinthe.MUR].append((ligne, colonne))
        elif case == ".":
            labyrinthe.grille[Labyrinthe.PORTE_OUVERTE].append((ligne, colonne))
        elif case == 'U':
            labyrinthe.sortie = (ligne, colonne)
        elif case == ' ':
            labyrinthe.grille[Labyrinthe.VIDE].append((ligne, colonne))
        colonne += 1
    labyrinthe.nb_lignes = ligne+1
    return labyrinthe


class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = creer_labyrinthe_depuis_chaine(chaine)

    def ajouter_joueur(self):
        robot_pos = random.choice(self.labyrinthe.grille[Labyrinthe.VIDE])
        self.labyrinthe.robot.append(robot_pos)

    def __repr__(self):
        represent = ""
        ligne = 0
        colonne = 0
        while ligne < self.labyrinthe.nb_lignes:
            while colonne < self.labyrinthe.nb_colonnes:
                if (ligne, colonne) in self.labyrinthe.grille[Labyrinthe.MUR]:
                    represent += 'O'
                elif (ligne, colonne) in self.labyrinthe.robot:
                    represent += 'X'
                elif (ligne, colonne) == self.labyrinthe.sortie:
                    represent += 'U'
                elif (ligne, colonne) in self.labyrinthe.grille[Labyrinthe.PORTE_OUVERTE]:
                    represent += '.'
                else:
                    represent += ' '
                colonne += 1
            ligne += 1
            colonne = 0
            represent += '\n'
        return represent

