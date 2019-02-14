"""
The interface takes the game into its hand and launch actions how they are needed
with this interface...
"""

class ConsoleInterface():

    def __init__(self,game):
        self.game = game

    def afficherLigne(self, n) :
        for i in range(n) :
            print("I", end = "")
        print("")

    def waitForStrategy(self):
        line = int(input("vous voulez jouer sur la ligne : ")) -1
        nbMatches = int(input("combien d'allumettes voulez vous retirer ? :  "))
        while not self.game.isValidStrategy(line, nbMatches) :
            print ("Erreur : choix non valide, ")
            line = int(input("choisiez une ligne : ")) -1
            nbMatches = int(input(" combien d'allumette voulez vous retirer ? :  "))

        return line, nbMatches

    def displayBoard(self) :
        """
        display the board
        """
        board = self.game.getBoard()
        for i in range(len(board)) :
            print(i + 1,":  ", end="")
            self.afficherLigne(board[i])


    def play(self):

        # Début de la partie
        continuer = True
        while continuer :

            ## Affichage du plateau
            self.displayBoard()

            # On récupere le joueur en cours
            player = self.game.getPlayer()

            # Le Joueur choisit ce qu'il veut faire
            print (player.getName(), " a vous")
            nbLigne, nbAll = player.chooseStrategy()

            ## retrait des Allumettes
            self.game.drawMatches(nbLigne,nbAll)

            ## Changement de joueur
            self.game.changePlayer()

            if self.game.isFinished() :
                continuer = False

        print("joueur", self.game.getNumPlayer(),self.game.getPlayer().getName(),"a gagné ")
