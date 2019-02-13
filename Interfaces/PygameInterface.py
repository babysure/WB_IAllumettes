import pygame

class PygameInterface():
    """
    Pygame interface for the marienbad game
    """
    def __init__(self,game):
        self.game = game

        ## Initialisation de la fenetre et création
        pygame.init()
        #creation de la fenetre

        self.largeur = 640
        self.hauteur = 480
        self.fenetre=pygame.display.set_mode((self.largeur,self.hauteur))

        ## Lecture des differentes images.


        self.images = {}
        self.images["allumette"] = pygame.image.load("Interfaces/allumette.png").convert_alpha()
        self.images["fond"] = pygame.image.load("Interfaces/backgroundimage_v3.jpg").convert_alpha()


        self.eventQuit = False
        self.quitGame = False

        fini = self.game.isFinished()
        numJoueur = self.game.getNumPlayer()

        plateau = self.game.getBoard()
        self.rectButtons = self.afficher(plateau,self.images, numJoueur,fini)




    def play(self):

        fini = self.game.isFinished()
        numJoueur = self.game.getNumPlayer()

        plateau = self.game.getBoard()

        # Boucle des tours de jeu
        horloge = pygame.time.Clock()

        while self.quitGame == False:
            # on fixe la cadence
            horloge.tick(20)

            # on r�cup�re la pile d'evenements pour plus tard.
            allEvents = pygame.event.get()

            # on r�cup�re aussi l'�tat des touches pour plus tard.
            touches = pygame.key.get_pressed();

            player = self.game.getPlayer()

            # Quand on joue (sinon, on est entre deux parties)
            if not self.game.isFinished():


                if player.needInputInterface():
                    # On vide la pile d'evenements et on verifie certains evenements
                    for event in allEvents:   # parcours de la liste des evenements recus

                        if event.type == pygame.MOUSEBUTTONUP:     #Si on relache la souris
                            ## on va parcourir les rectangles pour savoir lequel a �t� cliqu�

                            for i in range(len(plateau)):
                                for j in range(len(self.rectButtons[i])):
                                    if self.rectButtons[i][j].collidepoint(event.pos):
                                        #print "choix : ligne ",i, "nb all ", j
                                        numLigne = i
                                        nbAllumettes = j+1
                                        self.game.drawMatches(numLigne,nbAllumettes)
                                        plateau = self.game.getBoard()

                                        self.game.changePlayer()
                else :
                    ## This is an IA playing
                    nbLigne, nbAll = player.chooseStrategy()
                    self.game.drawMatches(nbLigne,nbAll)
                    plateau = self.game.getBoard()

                    self.game.changePlayer()


            else :  #(entre deux parties)
                if touches[pygame.K_SPACE] :
                    self.game.newGame()
                    plateau = self.game.getBoard()

                    fini = False

            fini = self.game.isFinished()
            numJoueur = self.game.getNumPlayer()

            # quoi qu'il en soit, on affiche le plateau
            self.rectButtons = self.afficher(plateau,self.images,numJoueur, fini)



            # et on v�rifie si on a voulu quitter
            for event in allEvents:   # parcours de la liste des evenements recus
                    if event.type == pygame.QUIT:     #Si un de ces evenements est de type QUIT
                        self.quitGame = True

        pygame.quit()


    ## La fonction d'affichage du plateau
    def afficher(self,tab, images,numJoueur, fini):
        # Choix de la police pour le texte
        font = pygame.font.Font(None, 34)

        # Affichage du fond
        rectFond = self.images["fond"].get_rect()
        self.fenetre.blit(images["fond"], rectFond)

        # Affichage du num�ro du joueur
        imageText = font.render("Joueur "+str(numJoueur), True, (255, 0, 0))
        rectText = imageText.get_rect()
        rectText.x = 500
        rectText.y = 30
        self.fenetre.blit(imageText, rectText)

        if fini :
            imageText = font.render("gagne !", True, (255, 0, 0))
            rectText = imageText.get_rect()
            rectText.x = 500
            rectText.y = 60
            self.fenetre.blit(imageText, rectText)

            imageText = font.render("Space pour recommencer", True, (255, 255, 255))
            rectText = imageText.get_rect()
            rectText.centerx = self.largeur/2
            rectText.centery = self.hauteur/2
            self.fenetre.blit(imageText, rectText)

        xOffset = 200
        # affichage des allumettes
        rectAllu = self.images["allumette"].get_rect()

        # la position des rectangles de choix possible est stock�e
        rectChoix = []

        for i in range(len(tab)):
            rectChoix.append([])
            # Position verticale de la ligne dans la fenetre
            rectAllu.y = (rectAllu.h+ 10) *i + 10


            # Affichage des choix de suppression possible
            #   on peut afficher de 1 a 3 (ou de 1 a tab[i] si tab[i]<3)

            nbButtons = min(3,tab[i])

            for n in range(0, nbButtons) :

                imageText = font.render(str(n+1), True, (255, 255, 255))
                rectText = imageText.get_rect()
                rectText.centery = rectAllu.centery
                rectText.x = xOffset + n*(rectText.w+10)

                rectChoix[i].append(rectText)

                self.fenetre.blit(imageText, rectText)



            for j in range(tab[i]):
                rectAllu.x = (rectAllu.w+20)*j + xOffset + 100
                self.fenetre.blit(images["allumette"], rectAllu)

        # raffraichissement
        pygame.display.flip()



        return rectChoix
