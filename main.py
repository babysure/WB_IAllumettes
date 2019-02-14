
from Agents.GenericAgent import *
from Agents.Human import *
from Agents.BasicMinMax import *

from Interfaces.ConsoleInterface import *
from Interfaces.PygameInterface import *

from game import Game

def main():

    # Création de la partie (initialisation, tout ca)
    game = Game()

    # Choix d'une interface pour jouer
    interface = PygameInterface(game)

    ## Création des Joueurs et ajout des joueurs a la partie
    player = Human(game,interface)
    game.addPlayer(player)

    player = BasicMinMax(game,interface)
    game.addPlayer(player)



    # lancement du jeu
    interface.play()


if __name__ == "__main__":
    main()
