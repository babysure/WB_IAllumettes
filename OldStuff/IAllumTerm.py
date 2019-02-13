
from random import randint

from fonctionsIA import *
from fonctionsJeu import *




def Jeu(Joueur, tableau):


    if Joueur != "IA":
        print("")
        print(Joueur,"c'est à vous")

        ligne = int(input("vous voulez jouer sur la ligne : ")) -1
        while   (ligne <= -1) or (ligne >= 4 )   :
             ligne = int(input("erreur: choisiez une autre ligne : ")) -1

        while tableau[ligne] <= 0 :
            ligne = int(input("erreur: choisiez une autre ligne :  ")) -1



        allumette = int(input("combien d'allumette voulez vous drawMatches ? :  "))
        while (allumette <=0) or (allumette >= 4) :
                allumette = int(input(" erreur: combien d'allumette voulez vous drawMatches ? :  "))

        while allumette > tableau[ligne] :
                allumette = int(input(" erreur: combien d'allumette voulez vous drawMatches ? :  "))
    else:
        ligne , allumette = evalueEtChoisit(tableau)
        print("je retire ", allumette," sur la ligne ", ligne +1)




    tableau[ligne] = tableau[ligne] - allumette
    afficherTab(tableau)
    #si c'est l'IA qui joue




tableau = [1 , 3 , 5 , 7]
continuer = True
afficherTab(tableau)
joueur1 = input("comment vous  appellez-vous Joueur 1:  ")
#on va faire en sorte que le joueur 2 c'est l'IA
"""
joueur2 = input("comment vous appellez-vous Joueur 2:  ")

"""
joueur2 = "IA"

#on choisie de façon aléatoire le premier joueur
def choix_joueur(joueur1,joueur2):
    if randint(0,1) == 0:
        c = joueur1
        joueur1 = joueur2
        joueur2 = c
    return joueur1 , joueur2

joueur1 , joueur2 = choix_joueur(joueur1,joueur2)


while continuer :

    Jeu(joueur1, tableau)
    if countMatches(tableau) == 0 :
        continuer = False
        print(joueur1,"vous avez perdu")

    if continuer:
        Jeu(joueur2, tableau)
        if countMatches(tableau) == 0 :
            continuer = False
            print(joueur2,"vous avez perdu")
