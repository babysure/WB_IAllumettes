# Le Jeu des allumettes et ses IA

Pour l'utiliser, lancer simplement

```bash
python main.py
```

## Organisation du dépôt

- *main.py* contient le code du jeu des Allumettes
- *game.py* est la classe en charge de la partie
(elle affiche, compte des allumettes...)
- Le repertoire *Agents* contient les fichiers de chaque type de joueur possible.
Pour le moment, il y en a trois :
  - GenericAgent : La classe dont dérivent les autres
  - HumanPlayer : un joueur humain
  - BasicMinMax : une IA simple
Je compte bien ajouter une IA utilisant des reseaux de neurones sous peu...
- Le repertoire *Interfaces* contient les fichiers de chaque type d'interface possible.
Pour le moment, il y en a deux :
  - ConsoleInterface : le jeu s'affiche en ligne de commande
  - PygameInterface : le jeu utilise une interface pygame


## Les Agents (types de joueurs) :

Ils doivent implémenter une méthode
- getName : qui renvoie leur nom.
- chooseStrategy : qui renvoie, pour une situation donnée leur choix (ligne et nombre d'allumettes)


That's all
