

from Agents.HumanPlayer import *
from Agents.BasicMinMax import *
from game import Game

def main():

    # Creation du plateau Initial (1, 3, 5, 7)
    game = Game()

    ## Définition des Joueurs
    # la ligne suivante pour permet d'avoir un humain contre une IA)
    #players = [HumanPlayer(game), BasicMinMax(game)]

    # la ligne suivante pour permet d'avoir une IA contre une IA)
    players = [BasicMinMax(game,"1"), BasicMinMax(game,"2")]

    # numéro du joueur en cours
    numPlayer = 0

    # Début de la partie
    continuer = True
    while continuer :

        ## Affichage de la partie
        game.afficher()

        # Le joueur en cours est dans le tableau des joueurs
        player = players[numPlayer]

        # Le Joueur choisit ce qu'il veut faire
        print (player.getName(), " a vous")
        nbLigne, nbAll = player.chooseStrategy()

        ## retrait des Allumettes
        game.retirer(nbLigne,nbAll)

        ## Changement de joueur
        numPlayer = (numPlayer+1)%2

        if game.estVide() :
            continuer = False

    print(players[numPlayer].getName()," a gagné ")



if __name__ == "__main__":
    main()
