

from Agents import HumanPlayer
from Agents import BasicMinMax
from board import Board

def main():

    # Creation du plateau Initial (1, 3, 5, 7)
    tableau = Board()

    # Définition des Joueurs (Ici, un humain contre une IA)
    #players = [HumanPlayer.HumanPlayer(tableau), BasicMinMax.BasicMinMax(tableau)]
    players = [BasicMinMax.BasicMinMax(tableau,"1"), BasicMinMax.BasicMinMax(tableau,"2")]

    # numéro du joueur en cours
    numPlayer = 0

    # Début de la partie
    continuer = True
    while continuer :

        ## Affichage du tableau
        tableau.afficher()

        # Le joueur en cours est dans le tableau des joueurs
        player = players[numPlayer]

        # Le Joueur choisit ce qu'il veut faire
        print (player.getName(), " a vous")
        nbLigne, nbAll = player.chooseStrategy()

        ## retrait des Allumettes
        tableau.retirer(nbLigne,nbAll)

        ## Changement de joueur
        numPlayer = (numPlayer+1)%2

        if tableau.estVide() :
            continuer = False

    print(players[numPlayer].getName()," a gagné ")



if __name__ == "__main__":
    main()
