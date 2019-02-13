class HumanPlayer():
    def __init__(self,game):
        self.nom = input("comment vous  appellez-vous ?")
        self.game = game


    def getName(self):
        return self.nom

    def chooseStrategy(self):

        tableau = self.game.getBoard()

        ligne = int(input("vous voulez jouer sur la ligne : ")) -1
        while   (ligne <= -1) or (ligne >= 4 )   :
            ligne = int(input("erreur: choisiez une autre ligne : ")) -1

        allumette = int(input("combien d'allumettes voulez vous retirer ? :  "))
        while (allumette <=0) or (allumette >= 4) or allumette > tableau[ligne] :
                allumette = int(input(" erreur: combien d'allumette voulez vous retirer ? :  "))

        return ligne, allumette
