import copy

class BasicMinMax():
    def __init__(self, game,name):
        self.nom = "Basic MinMax IA "+ name
        self.game = game


    def getName(self):
        return self.nom

    def chooseStrategy(self):

        bestResult = -2
        choixBestLigne = -1
        choixBestNb = -1

        tableau = self.game.getBoard()
        ## Am I playing ? (sure)
        me = True

        for choixNb in [1,2,3]:
            for choixLigne in [0,1,2,3]:

                if (tableau[choixLigne] - choixNb >= 0) and bestResult < 1 :
                    # on copie le plateau
                    plateauTemp = copy.deepcopy(tableau)

                    plateauTemp[choixLigne]-= choixNb
                    #print(plateauTemp)

                    # calling evaluation and I won't play
                    resu = self.evaluate(plateauTemp, not me )
                    #print (resu)
                    if resu > bestResult :
                        choixBestLigne = choixLigne
                        choixBestNb = choixNb
                        bestResult = resu
                        #print (bestResult, choixBestLigne, choixBestNb)

        print("je retire ", choixBestNb, " sur la ligne ",choixBestLigne+1, "et ")

        if (bestResult==1) :
            print("Je vais gagner")
        else:
            print ("je perdrais si tu joues bien")

        return choixBestLigne, choixBestNb

    def evaluate(self, plateau, me):
        if self.game.estVide(plateau) :
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

            for choixLigne in [0,1,2,3]:
                for choixNb in [1,2,3]:
                    if (plateau[choixLigne] -choixNb >= 0 and resu != targetResu) :
                        # on copie le plateau
                        plateauTemp = copy.deepcopy(plateau)

                        plateauTemp[choixLigne]-= choixNb

                        resu = self.evaluate(plateauTemp, not me)

                        resuDessous.append(resu)

            if me:
                resuVrai = max(resuDessous)
            else :
                resuVrai = min(resuDessous)

            #on récupère l'indices d

        #print (plateau, resuVrai, ligneVraie, nbAllVraie)
        return resuVrai
