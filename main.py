
from Agents.GenericAgent import *
from Agents.Human import *
from Agents.BasicMinMax import *

from game import Game

def main():

    # Creation du plateau Initial (1, 3, 5, 7)
    game = Game()

    ## Définition des Joueurs
    # la ligne suivante pour permet d'avoir un humain contre une IA)

    # la ligne suivante pour permet d'avoir une IA contre une IA)
    game.addPlayer(Human(game))
    game.addPlayer(BasicMinMax(game))

    # Début de la partie
    continuer = True
    while continuer :

        ## Affichage de la partie
        game.afficher()

        # On récupere le joueur en cours
        player = game.getPlayer()

        # Le Joueur choisit ce qu'il veut faire
        print (player.getName(), " a vous")
        nbLigne, nbAll = player.chooseStrategy()

        ## retrait des Allumettes
        game.retirer(nbLigne,nbAll)

        ## Changement de joueur
        game.changePlayer()

        if game.estVide() :
            continuer = False

    print("joueur", game.getNumPlayer(),game.getPlayer().getName(),"a gagné ")



if __name__ == "__main__":
    main()
