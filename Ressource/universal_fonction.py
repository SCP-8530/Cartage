###########################################################################
### DEV: The_Am0nnal13
### Description du fichier: Liste de fonction intervenant dans differents fichier du programme
###########################################################################

#################
### PROGRAMME ###
#################
#fonction de wait
def Wait():
    try:
        input('Appuyer sur Entrée pour continuer...')
    except SyntaxError:
        pass

#fonction de clear
def ClearConsole():
    n = 0
    while n < 50:
        print(f"\n")
        n += 1

#Class couleur
class mycolor:
    W  = '\033[0m'  # white (normal)
    R  = '\033[31m' # red
    G  = '\033[32m' # green
    O  = '\033[33m' # orange
    B  = '\033[34m' # blue
    P  = '\033[35m' # purple

#fonction de couleur d'interface client
def InterfaceColor(Couleur): # mettre une couleur a l'interface
    if Couleur == "W":
        print(f"{mycolor.W}")
    elif Couleur == "R":
        print(f"{mycolor.R}")
    elif Couleur == "G":
        print(f"{mycolor.G}")
    elif Couleur == "O":
        print(f"{mycolor.O}")
    elif Couleur == "B":
        print(f"{mycolor.B}")
    elif Couleur == "P":
        print(f"{mycolor.P}")