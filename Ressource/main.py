#Fontion import
from fonction_main import *
from universal_fonction import *
import webbrowser as wb

#mettre en pleine ecran
print("Pour une meilleur experience il est conseiller de passer en mode pleine ecran.")
Wait()
ClearConsole()

#Page de connexion au systeme
print(
        f"{mycolor.P}##########################################\n"
        f"#{mycolor.W}   Bienveunue dans le systeme Cartage   {mycolor.P}#\n"
        f"##########################################\n"
        f"#{mycolor.W}     Veiller donner votre matricule     {mycolor.P}#\n"
        f"##########################################\n{mycolor.W}"
    )
l = input(">>> ")

#data de detection de compte
tf = open("Data\lstMat.json", "r")
RR = json.load(tf, object_hook=dict)

#Detecter le compte
if l in RR.keys():
    #detecter les autorisations du compte
    if RR[l][0] == "U":
        LOGIN = "U"
    elif RR[l][0] == "A":
        LOGIN = "A"
    #en cas de personne inconnue au systeme
elif l == "<3":
    wb.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    LOGIN = "E"
else:
    print("Vous ne faite pas parti du systeme Cartage.\nVeuiller contacter CR2429 ou Messio (F4) si il ne vous a pas ajouter.")
    LOGIN = "E"

 
#redirection
if LOGIN == "A":
    LogA(l)
elif LOGIN == "U":
    LogU(l)

#fermer l'application
print(f"\n\nMerci d'avoir utiliser le systeme cartage.")
#END
#Dev: Guillaume Paoli (CR2429)