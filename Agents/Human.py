import sys
import os

currentDir = os.path.dirname(os.path.abspath(__file__))
upperDir = os.path.dirname(currentDir)
sys.path.append(upperDir)

from Agents.GenericAgent import *

class Human(GenericAgent):
    def __init__(self,game):
        GenericAgent.__init__(self,game)
        self.nom = input("comment vous  appellez-vous ?")

    def chooseStrategy(self):

        tableau = self.game.getBoard()

        ligne = int(input("vous voulez jouer sur la ligne : ")) -1
        while   (ligne <= -1) or (ligne >= 4 or tableau[ligne] <= 0)   :
            ligne = int(input("erreur: choisiez une autre ligne : ")) -1

        allumette = int(input("combien d'allumettes voulez vous retirer ? :  "))
        while (allumette <=0) or (allumette >= 4) or allumette > tableau[ligne] :
                allumette = int(input(" erreur: combien d'allumette voulez vous retirer ? :  "))

        return ligne, allumette
