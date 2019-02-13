
from Agents.GenericAgent import *
from Agents.Human import *
from Agents.BasicMinMax import *

from game import Game

def main():

    # Création de la partie (initialisation, tout ca)
    game = Game()

    ## Création des Joueurs et ajout des joueurs a la partie
    player = Human(game)
    game.addPlayer(player)

    player = BasicMinMax(game)
    game.addPlayer(player)

    # Début de la partie
    continuer = True
    while continuer :

        ## Affichage du plateau
        game.display()

        # On récupere le joueur en cours
        player = game.getPlayer()

        # Le Joueur choisit ce qu'il veut faire
        print (player.getName(), " a vous")
        nbLigne, nbAll = player.chooseStrategy()

        ## retrait des Allumettes
        game.drawMatches(nbLigne,nbAll)

        ## Changement de joueur
        game.changePlayer()

        if game.isFinished() :
            continuer = False

    print("joueur", game.getNumPlayer(),game.getPlayer().getName(),"a gagné ")



if __name__ == "__main__":
    main()
