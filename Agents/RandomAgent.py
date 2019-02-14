import copy

import sys
import os
import random

currentDir = os.path.dirname(os.path.abspath(__file__))
upperDir = os.path.dirname(currentDir)
sys.path.append(upperDir)

from Agents.GenericAgent import *


class RandomAgent(GenericAgent):
    """The class for a stupid IA that acts at random

    """
    def __init__(self, game, interface):
        """
        Create a RandomAgent.
        it's name is defined as "Stupid IA"
        """
        GenericAgent.__init__(self,game,interface)
        self.setName("Stupid IA")

    def chooseStrategy(self):
        """
        Ask the IA what it wants to play (line and number of matches)

        I should probably explain how it works...
        """

        # Get all possible choices
        strategies = self.game.getValidNextStrategies()

        # Draw one.
        choice = random.randrange(len(strategies))
        line = strategies[choice][0]
        nbMatches = strategies[choice][1]

        return line, nbMatches
