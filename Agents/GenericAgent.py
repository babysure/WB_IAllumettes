


class GenericAgent():
    """The parent class of all Agents
    An Agent is a player, either an IA or a human player.
    It is involved in a Game and must be created with one existing game.
    It is given an interface to communicate with.

    An Agent has :
    - a name
    - a number as a player (given by its insertion in a Game)

    Every Agent should define its own strategy
    """
    def __init__(self, game,interface):
        """
        Create a Generic Agent involved in a Game
        """
        self.name = "I'm generic. I should not be used "
        self.game = game  # the player is involved in this game"""
        self.num = -2     # Number of the player in the game (0 or 1)"""
        self.interface = interface

    def setNum(self,num):
        """
        Set the number of the player in the current game
        """
        self.num=num

    def getNum(self,num):
        """
        Get the number of the player in the current game
        """
        return self.num

    def getName(self):
        """
        Get the name of the player
        """
        return self.nom

    def setName(self, name):
        """
        Set the name of the player
        """
        self.nom = name

    def chooseStrategy(self):
        """
        Compute a strategy (Number of matches and line) that the agent would like to
        play.

        Returns line, nbMatches
        """
        print ("I don't have any strategy, I'll return 1,1")

        return 1,1

    def needInputInterface(self):
        """
        tell if the Agent needs an input interface to define his strategy
        only Human agents should set this to True
        """
        return False
