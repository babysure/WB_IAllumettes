import copy

import sys
import os

currentDir = os.path.dirname(os.path.abspath(__file__))
upperDir = os.path.dirname(currentDir)
sys.path.append(upperDir)

from Agents.GenericAgent import *


class BasicMinMax(GenericAgent):
    """The class for a Pure Tree IA using Min Max Strategy

    """
    def __init__(self, game):
        """
        Create a BasicMinMax.
        it's name is defined as "Basic MinMax IA"
        """
        GenericAgent.__init__(self,game)
        self.setName("Basic MinMax IA")

    def chooseStrategy(self):
        """
        Ask the IA what it wants to play (line and number of matches)

        I should probably explain how it works...
        """
        bestResult = -2
        choixBestLigne = -1
        choixBestNb = -1

        tableau = self.game.getBoard()

        ## Am I playing ? (sure)
        me = True

        strategies = self.game.getValidNextStrategies()

        for strategy in strategies :
            line = strategy[0]
            nbMatches = strategy[1]

            if bestResult < 1 :
                # on copie le plateau
                plateauTemp = copy.deepcopy(tableau)

                plateauTemp[line]-= nbMatches
                #print(plateauTemp)

                # calling evaluation and I won't play
                resu = self.evaluate(plateauTemp, not me )

                #print (resu)
                if resu > bestResult :
                    choixBestLigne = line
                    choixBestNb = nbMatches
                    bestResult = resu
                    #print (bestResult, choixBestLigne, choixBestNb)

        print("je retire ", choixBestNb, " sur la ligne ",choixBestLigne+1, "et ")

        if (bestResult==1) :
            print("Je vais gagner")
        else:
            print ("je perdrais si tu joues bien")

        return choixBestLigne, choixBestNb

    def evaluate(self, plateau, me):
        """
        Internal evaluation of sub configurations of the game. Yep, recursive.

        I should probably explain how it works...
        """
        if self.game.isFinished(plateau) :
            if me :
                resuVrai = 1
            else :
                resuVrai = -1
        else :

            resuDessous =[]
            resu = -2
            if me:
                targetResu  = 1
            else :
                targetResu  = -1

            strategies = self.game.getValidNextStrategies(plateau)

            for strategy in strategies :
                line = strategy[0]
                nbMatches = strategy[1]

                if resu != targetResu :
                    # on copie le plateau
                    plateauTemp = copy.deepcopy(plateau)

                    plateauTemp[line]-= nbMatches

                    resu = self.evaluate(plateauTemp, not me)

                    resuDessous.append(resu)

            if me:
                resuVrai = max(resuDessous)
            else :
                resuVrai = min(resuDessous)

            #on récupère l'indices d

        #print (plateau, resuVrai, ligneVraie, nbAllVraie)
        return resuVrai
