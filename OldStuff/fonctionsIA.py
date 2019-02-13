from fonctionsJeu import *




def evalue(plateau, joueur, IA):
    if countMatches(plateau) == 0 :
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
