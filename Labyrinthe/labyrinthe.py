# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:
    MUR = 'mur'
    PORTE_OUVERTE = 'porte ouverte'
    PORTE_FERMEE = 'porte fermee'
    VIDE = 'vide'
    error = "La commande doit être au format {N, E, S, O} plus un nombre, ou Q, ou {M, P} plus {N, E, S, O}."

    """Classe représentant un labyrinthe."""

    def __init__(self, sortie=(0, 0)):
        self.robot = []
        self.grille = {Labyrinthe.MUR: [], Labyrinthe.PORTE_OUVERTE: [], Labyrinthe.PORTE_FERMEE: [], Labyrinthe.VIDE: []}
        self.nb_colonnes = 0
        self.nb_lignes = 0
        self.sortie = sortie

    #Ajoute un robot au hasard dans une case vide
    def ajouter_robot(self):
        pass

    def jouer(self, commande, robot):
        """commande est un string. Entrée d'un input()
        renvoie False pour arrêter le jeu"""

        #On vérifie la commande
        if len(commande) == 0:
            raise AssertionError(Labyrinthe.error)
        #Quitter
        if commande[0] in 'qQ':
            return False
        #Murage ou perçage de porte
        if len(commande) == 2 and commande[0] in 'mpMP' and commande[1] in 'nesoNESO':
            pass
        #Direction simple
        elif len(commande) == 1 and commande[0] in 'nesoNESO':
            self.move_robot(commande[0], 1, robot)
        #Direction multiple
        elif len(commande) > 1 and commande[0] in 'nesoNESO':
            try:
                #On récupère le nombre de pas
                nombre = int(commande[1:])
                self.move_robot(commande[0], nombre, robot)
            except ValueError:
                raise AssertionError(Labyrinthe.error)
        else:
            raise AssertionError(Labyrinthe.error)
        return True

    def gagne(self):
        for i, rob in enumerate(self.robot):
            if rob == self.sortie:
                return i

    def move_robot(self, direction, nombre, robot):
        nb_pas = 0
        while nb_pas < nombre:
            self.try_move_robot(direction, robot)
            nb_pas += 1

    def try_move_robot(self, direction, robot):
        direction = direction.upper()
        if direction == 'N':
            x = 0
            y = 1
            step = -1
            fun = int.__ge__
            bound = 0
        if direction == 'S':
            x = 0
            y = 1
            step = 1
            fun = int.__le__
            bound = self.nb_lignes
        if direction == 'E':
            x = 1
            y = 0
            step = 1
            fun = int.__le__
            bound = self.nb_colonnes
        if direction == 'O':
            x = 1
            y = 0
            step = -1
            fun = int.__ge__
            bound = 0
        if fun(self.robot[robot][x] + step, bound) and not (self.robot[robot][x] + step, self.robot[robot][y]) in self.grille[Labyrinthe.MUR]:
            if direction in "OE":
                self.robot[robot] = (self.robot[robot][0] + step, self.robot[robot][1])
            else:
                self.robot[robot] = (self.robot[robot][0], self.robot[robot][1] + step)


