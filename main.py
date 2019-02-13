
from Agents.GenericAgent import *
from Agents.Human import *
from Agents.BasicMinMax import *

from Interfaces.ConsoleInterface import *
from Interfaces.PygameInterface import *

from game import Game

def main():

    # Création de la partie (initialisation, tout ca)
    game = Game()

    ## Création des Joueurs et ajout des joueurs a la partie
    player = Human(game)
    game.addPlayer(player)

    player = BasicMinMax(game)
    game.addPlayer(player)

    # Choix d'une interface pour jouer
    interface = PygameInterface(game)

    # lancement du jeu
    interface.play()


if __name__ == "__main__":
    main()
