
class GenericAgent():
    def __init__(self, game):
        self.nom = "I'm generic. I should not be used "
        self.game = game
        self.num = -2

    def setNum(self,num):
        self.num=num

    def getNum(self,num):
        return self.num

    def getName(self):
        return self.nom

    def chooseStrategy(self):
        print ("I don't have any strategy, I'll return 1,1")

        return 1,1
