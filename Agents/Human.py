import sys
import os

currentDir = os.path.dirname(os.path.abspath(__file__))
upperDir = os.path.dirname(currentDir)
sys.path.append(upperDir)

from Agents.GenericAgent import *

class Human(GenericAgent):
    """The class for Human Agents
    A Human is a GenericAgent that wil be asked is own strategy via the interface
    of the game.

    At its creation, the user is asked to enter the Human name via the interface

    """
    def __init__(self,game,interface):
        """
        Create a Human.
        Ask the user it's name to define the Agent name.
        """
        GenericAgent.__init__(self,game,interface)
        self.nom = input("comment vous  appellez-vous ?")

    def chooseStrategy(self):
        """
        Returns the strategy (Number of matches and line) that the human player
        would like to play. The user is asked what his strategy is.

        Returns line, nbMatches
        """

        tableau = self.game.getBoard()
        line, nbMatches = self.interface.waitForStrategy()

        return line, nbMatches

    def needInputInterface(self):
        """
        tell if the Agent needs an input interface to define his strategy
        only Human agents should set this to True
        """
        return True
