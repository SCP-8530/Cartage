###########################################################################
### DEV: The_Am0nnal13
### Description du fichier: Fichier qui gere l'autentification de l'utilisateur et son interface client
###########################################################################

###################
### IMPORTATION ###
###################
from universal_fonction import *
import webbrowser as wb
from fonction_admin import *
from fonction_client import *
import json
from universal_fonction import *

################################
### DEFINITION DES FONCTIONS ###
################################
def LogA(l):
    '''
    Interface administateur
    '''

    ClearConsole()
    while True:
        #Affichage du menu
        print(
            f"\n{mycolor.W}*************************"
            f"\n* Menu de l'application *"
            f"\n*************************"
            f"\n1. Ajouter un Matricule"
            f"\n2. Afficher la liste des Crystaliens"
            f"\n3. Modifier un Matricule"
            f"\n4. Supprimer un Matricule"
            f"\n5. Ajouter un mission"
            f"\n6. Liste des missions"
            f"\n7. Passer en mode client"
            f"\n0. Fermer l'application"
        )

        #interactoion avec le menu
        reponse = str(input(">>> "))

        if reponse == "1": #Ajout de matricule
            ClearConsole()

            #Verification du code
            Matricule = str(input("Entré le matricule du crystalien: "))
            tf = open("Data\lstCrystalien.json", "r")
            RR = json.load(tf, object_hook=dict)

            if Matricule in RR.keys():
                ClearConsole()
                print(f"{mycolor.R}Desoler mais le matricule semble deja present")
            else:
                tf.close()

                AjoutCR(Matricule)
        
        elif reponse == "2": #Afficher la liste des Crystaliens
            AfficherLstCR()

        elif reponse == "3": #Modifier un Matricule
            #Verification du code
            Matricule = str(input(f"\n\nEntré le matricule du crystalien: "))
            tf = open("Data\lstCrystalien.json", "r")
            RR = json.load(tf, object_hook=dict)
            tf.close()
            if Matricule in RR.keys():
                ModifCR(RR, Matricule)
            else:
                ClearConsole()
                print(f"{mycolor.R}Desoler mais le matricule semble ne pas existé")

        elif reponse == "4": #Supprimer un Matricule
            
            #Verification du code
            Matricule = str(input(f"\n\nEntré le matricule du crystalien: "))
            tf = open("Data\lstCrystalien.json", "r")
            RR = json.load(tf, object_hook=dict)
            tf.close()
            if Matricule in RR.keys():
                SupprCR(Matricule)
            else:
                ClearConsole()
                print(f"{mycolor.R}Desoler mais le matricule semble ne pas existé{mycolor.W}")

        elif reponse == "5": #Ajouter un mission
            #Verification du code
            Matricule = str(input(f"\nEntré le matricule du crystalien: "))
            tf = open("Data\lstCrystalien.json", "r")
            RR = json.load(tf, object_hook=dict)

            if Matricule in RR.keys():
                AjoutMission(Matricule)
            else:
                ClearConsole()
                print(f"{mycolor.R}Desoler mais le matricule semble ne pas existé")            

        elif reponse == "6": #Liste des missions
            AfficherMission()

        elif reponse == "7": #Passer en mode client
            LogU(l)
        
        elif reponse == "0": #Fermer l'application
            break    

        else:
            #En cas de reponse non valide
            print(f"{mycolor.R}Réponse invalide. Veuiller choisir un chiffre entre 0 et 9")

def LogU(l):
    '''
    interface client
    '''
    ClearConsole()

    #coloration de l'interface utilisateur
    tf = open("Data\lstMat.json", "r")
    identifyColor = json.load(tf, object_hook=dict)
    tf.close
    Couleur = identifyColor[l][1]

    #definir la couleur
    InterfaceColor(Couleur)

    
    while True:
        #INTERFACE CLIENT
        print(
            f"\n╔══════════════════════════════╗"
            f"\n║{l:^30}║"
            f"\n╚══════════════════════════════╝"
            f"\n"
            f"\n╔════"
            f"\n║ Mission actif: {DetectMissionDetail(l)}"
            f"\n╚════"
            f"\n"
            f"\n╔════════════════════╦════════════════════╗"
            f"\n║{'1. Afficher toutes':^20}║{'2. Activer':^20}║"
            f"\n║{'vos missions':^20}║{'une mission':^20}║"
            f"\n╠════════════════════╬════════════════════╣"
            f"\n║{'3. Finir':^20}║{'4. Modifier':^20}║"
            f"\n║{'une mission':^20}║{'la couleur':^20}║"
            f"\n╠════════════════════╩════════════════════╣"
            f"\n║{'0. Fermer le systeme cartage':^41}║"
            f"\n╚═════════════════════════════════════════╝"
        )

        #CHOIX
        choix = str(input(">>> "))
        

        if choix == "1": #Montrer la liste complete des missions de l'utilisateur
            MontrerMission(l)
        
        elif choix == "2": #Activer une mission
            #detecter une mission actif
            if DetectMissionDetail(l) == "N/A":
                ActiveMission(l, Couleur)
            else:
                ClearConsole()
                print(f"▓▓▓ Vous avez deja une mission en cours. ▓▓▓")
    
        elif choix ==  "3": #finir une mission
            #detecter une mission actif
            if DetectMissionDetail(l) == "N/A":
                ClearConsole()
                print(f"▓▓▓ Vous n'avez aucune mission en cours. ▓▓▓")   
            else:
                ClearConsole()
                FinirMission(l)
        
        elif choix == "4": #Changer la couleur de l'interface
            paraCouleur(Couleur,l)
        
        elif choix == "0": #fermer l'interface client
            break
        
        else: #erreur de choix
            ClearConsole()
            print(f"▓▓▓ Choix non valide ▓▓▓")


    print(f"{mycolor.W}")


#################
### PROGRAMME ###
#################

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
elif l == "<3":
    wb.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    LOGIN = "E"
else:#en cas de personne inconnue au systeme
    print("Vous ne faite pas parti du systeme Cartage.\nVeuiller contacter CR2429 ou Messio (F4) si il ne vous a pas ajouter.")
    LOGIN = "E"

 
#redirection
if LOGIN == "A":
    LogA(l)
elif LOGIN == "U":
    LogU(l)

#fermer l'application
print(f"\n\nMerci d'avoir utiliser le systeme cartage.")
