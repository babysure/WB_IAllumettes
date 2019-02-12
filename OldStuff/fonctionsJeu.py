

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





def afficherLigne(n) :
	for i in range(n) :
		print("I", end = "")
	print("")



def afficherTab(tab) :
	print("")
	for i in range(len(tab)) :
		print(i + 1,":  ", end="")
		afficherLigne(tab[i])

