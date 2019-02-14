

import copy

class Game():
    """The class in charge of a Marienbad Game.

    It handles :
    - players and their turns
    - the board content
    """

    def __init__(self):
        """
        Create a Marienbad game and initialize the board.

        At the creation of the game, no player is involved in the game.
        They should be added later using addPlayer
        """
        self.board = [7 , 5, 3, 1]
        self.players=[]
        self.numJoueur = 0

    def newGame(self):
        self.board = [7 , 5, 3, 1]
        self.numJoueur = 0

    def addPlayer(self,player):
        """
        Add a player to the Game
        The player should be of one of the available types in Agents.

        The player is given a number in the game.
        """
        if len(self.players) <= 2 :
            # La partie fixe le numéro du joueur
            player.setNum(len(self.players))
            self.players.append(player)
        else :
            print("No more than 2 players !")

    def changePlayer(self):
        """
        Change the current player in the game
        """
        self.numJoueur = (self.numJoueur+1)%2

    def getPlayer(self):
        """
        get the current player in the game
        """
        return self.players[self.numJoueur]

    def getNumPlayer(self):
        """
        get the current player number in the game
        it will be 1 or 2.
        """
        return self.numJoueur+1

    def getBoard (self):
        """
        get a copy of the array that represents the board content.
        """
        newBoard = copy.deepcopy(self.board)
        return newBoard

    def getValidNextStrategies (self, board=None):
        """
        get an array of all possible strategy for the current state of the Board
        Each Strategy is a tuple containing (numLine, nbMatches)

        One could ask the ValidStrategies for a different board. If so,
        pass the board as a parameter
        """
        if board == None :
            board = self.board

        strategies = []
        for nbMatches in [1,2,3]:
            for line in [0,1,2,3]:
                if board[line] - nbMatches >= 0 :
                    strategies.append((line, nbMatches))

        return strategies

    def isValidStrategy (self, line, nbMatches, board=None):
        """
        test if a strategy is valid for the current state of the Board

        One could ask if a strategy is valid for a different board. If so,
        pass the board as a parameter
        """
        if board == None :
            board = self.board

        if (line < 0 or line >=4):
            return False

        if nbMatches < 1 or nbMatches >3 :
            return False

        if board[line]-nbMatches < 0:
            return False

        return True


    def isFinished (self, tab=None):
        """
        Tell if the game is finished or not
        (finished if no matches remains)
        """
        if self.countMatches(tab) == 0:
            return True
        return False

    def countMatches (self, tab=None):
        """
        Count matches on the board
        """
        if tab == None :
            tab = self.board

        nbAll =0
        for ligne in tab:
            if ligne >= 0:
                nbAll+=ligne
        return nbAll

    def drawMatches (self, line, nbMatches):
        """
        Draw some matches on the current board.

        It check if the proposal is valid.
        """
        if (self.isValidStrategy(line, nbMatches)) :
            self.board[line]-=nbMatches
        else :
            print ("You tried something bad")
