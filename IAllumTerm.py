
from random import randint


#on compte toutes les allumette qu'il y a sur sur le plateau 
def compteAllumettes (tab):
    nbAll =0
    for ligne in tab:
        if ligne >= 0:
            nbAll+=ligne
    return nbAll

#on change de joiueur 
def changerJoueur(joueur):
    if  joueur == 1:
        return 2
    return 1



def evalue(plateau, joueur, IA):
    if compteAllumettes(plateau) == 0 :
        if joueur == IA :
            resuVrai = 1
        else :
            resuVrai = -1
    else :

        resuDessous =[]
        resu = -2
        if joueur == IA:
            targetResu  = 1
        else :
            targetResu  = -1

        for choixLigne in [0,1,2,3]:
            for choixNb in [1,2,3]:
                if (plateau[choixLigne] -choixNb >= 0 and resu != targetResu) :
                    # on copie le plateau
                    plateauTemp = [] 
                    for nb in plateau :
                        plateauTemp.append(nb)
                    

                    plateauTemp[choixLigne]-= choixNb

                    resu = evalue(plateauTemp, changerJoueur(joueur),IA)

                    resuDessous.append(resu)                    
        
        if joueur == IA:
            resuVrai = max(resuDessous)
        else :
            resuVrai = min(resuDessous)

        #on récupère l'indices d
    
    #print (plateau, resuVrai, ligneVraie, nbAllVraie)
    return resuVrai

def evalueEtChoisit(plateau):
    bestResult = -2
    choixBestLigne = -1
    choixBestNb = -1

    joueur = 1
    IA = 1

    for choixNb in [1,2,3]:
        for choixLigne in [0,1,2,3]:
            
            if (plateau[choixLigne] - choixNb >= 0) and bestResult < 1 :
                # on copie le plateau
                plateauTemp = [] 
                for nb in plateau :
                    plateauTemp.append(nb)
                

                plateauTemp[choixLigne]-= choixNb
                #print(plateauTemp)

                resu = evalue(plateauTemp, changerJoueur(joueur),IA)
                #print (resu)
                if resu >= bestResult :
                    choixBestLigne = choixLigne
                    choixBestNb = choixNb
                    bestResult = resu
                    #print (bestResult, choixBestLigne, choixBestNb)                    
    
    if (bestResult==1) :
        print("Je gagne")
    else:
        print ("je perds si tu joues bien") 

    return choixBestLigne, choixBestNb


def afficherLigne(n) :
	for i in range(n) :
		print("I", end = "")
	print("")


def compteAllumette(tableau) :
        somme = tableau[0] + tableau[1] + tableau[2] + tableau[3]
        return somme 

def afficherTab(tab) :
	print("")
	for i in range(len(tab)) :
		print(i + 1,":  ", end="")
		afficherLigne(tab[i])



def Jeu(Joueur, tableau):
    
    
    if Joueur != "IA":
        print("")
        print(Joueur,"c'est à vous")

        ligne = int(input("vous voulez jouer sur la ligne : ")) -1
        while   (ligne <= -1) or (ligne >= 4 )   :
             ligne = int(input("erreur: choisiez une autre ligne : ")) -1

        while tableau[ligne] <= 0 :
            ligne = int(input("erreur: choisiez une autre ligne :  ")) -1



        allumette = int(input("combien d'allumette voulez vous retirer ? :  "))
        while (allumette <=0) or (allumette >= 4) :
                allumette = int(input(" erreur: combien d'allumette voulez vous retirer ? :  "))

        while allumette > tableau[ligne] :
                allumette = int(input(" erreur: combien d'allumette voulez vous retirer ? :  "))
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
    if compteAllumette(tableau) == 0 :
        continuer = False
        print(joueur1,"vous avez perdu")

    if continuer:
        Jeu(joueur2, tableau)
        if compteAllumette(tableau) == 0 :
            continuer = False
            print(joueur2,"vous avez perdu")
    
       



