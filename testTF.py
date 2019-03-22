from Agents.Model import *
from game import Game


# Création de la partie (initialisation, tout ca)
game = Game()

m =  Model(game)

board = [2,0,1,1]
player = 0
print (board, player)
print(m.make_feature_vector(board, player))


board = [6,4,3,1]
player = 1
print (board, player)
print(m.make_feature_vector(board, player))

resu = m.evaluate(board, player)
print (resu)