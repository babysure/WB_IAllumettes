import copy

class Board():
    def __init__(self):
        self.board = [7 , 5, 3, 1]


    def getBoard (self):
        newBoard = copy.deepcopy(self.board)
        return newBoard

    def estVide (self, tab=None):
        if self.compteAllumettes(tab) == 0:
            return True
        return False

    def compteAllumettes (self, tab=None):
        if tab == None :
            tab = self.board

        nbAll =0
        for ligne in tab:
            if ligne >= 0:
                nbAll+=ligne
        return nbAll

    def retirer (self, nbLigne, nbCol):
        if (self.board[nbLigne] >= nbCol) :
            self.board[nbLigne]-=nbCol
        else :
            print ("You tried something bad")

    def afficherLigne(self, n) :
        for i in range(n) :
            print("I", end = "")
        print("")


    def afficher(self) :
        print("")
        for i in range(len(self.board)) :
            print(i + 1,":  ", end="")
            self.afficherLigne(self.board[i])
