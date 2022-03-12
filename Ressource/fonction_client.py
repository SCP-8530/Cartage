###########################################################################
### DEV: The_Am0nnal13
### Description du fichier: Liste des fonction utiliser dans l'interface client
###########################################################################

###################
### IMPORTATION ###
###################
import json
from universal_fonction import *

#################
### PROGRAMME ###
#################
#Detecter une mission actif
def DetectMissionDetail(MAT):
    tf = open("Data\Mission.json", "r")
    Mission = json.load(tf, object_hook=dict)
    tf.close
    
    
    for index in range(0, len(Mission[MAT]), 1):
        if Mission[MAT][index][1] == "En cours...":
            Freturn = Mission[MAT][index][2]
            break
        else:
            Freturn = "N/A" 

    return Freturn

#Fonction 1
def MontrerMission(MAT):
    #recuperer les infos
    tf = open("Data\Mission.json", "r")
    Mission = json.load(tf, object_hook=dict)
    tf.close

    #afficher les infos
    
    print(f"\n\n\n########### Liste de toute vos missions ##########")
    for index in range(0, len(Mission[MAT]), 1):
        print(f"ID de la mission: {Mission[MAT][index][0]}")
        print(f"Etat de la mission: {Mission[MAT][index][1]}")
        print(f"Information sur la mission: {Mission[MAT][index][2]}")
        print("#" * 50)

    #fin de fonction
    Wait()
    ClearConsole()
        
#Fonction 2
def ActiveMission(MAT, Couleur):
    #recuperer les infos
    tf = open("Data\Mission.json", "r")
    Mission = json.load(tf, object_hook=dict)
    tf.close
    
    #afficher toute les missions inactive
    idMission = []

    print(f"\n\n\n########### Liste de toute vos missions ##########")
    for index in range(0, len(Mission[MAT]), 1):
        if Mission[MAT][index][1] == "Non-debuter":
            print(f"ID de la mission: {Mission[MAT][index][0]}")
            print(f"Etat de la mission: {Mission[MAT][index][1]}")
            print(f"Information sur la mission: {Mission[MAT][index][2]}")
            print("#" * 50)

            idMission.append(str(Mission[MAT][index][0]))

    #active une mission
    while True:
        #arreter la fonction si il y a pas de mission a activer
        if len(idMission) == 0:
            print("Vous n'avez aucune mission a faire.")
            break

        #Detecter l'id de la mission
        choix = str(input("Veuiller donner l'ID de la mission que vous souhaitez active:"))

        if choix in idMission:#id correcte
            for index in range(0, len(Mission[MAT]), 1):
                if Mission[MAT][index][0] == int(choix):
                    Mission[MAT][index][1] = "En cours..."
            print("Le choix a bien ete enregistrer")

            #enregistrement du choix
            tf = open("Data\Mission.json", "w")
            json.dump(Mission, tf, sort_keys=True, indent=4)
            tf.close
            #sorti de boucle
            break
        else:#id incorrecte
            print(f"▓▓▓ Cette ID de mission n'existe pas parmi vos missions ▓▓▓\n")
            
        
    #fin de fonction
    Wait()
    ClearConsole()

#Fonction 3
def FinirMission(MAT):
    #recuperer data
    tf = open("Data\Mission.json", "r")
    Mission = json.load(tf, object_hook=dict)
    tf.close

    #Changer l'etat de la mission
    for index in range(0, len(Mission[MAT]), 1):
        if Mission[MAT][index][1] == "En cours...":
            Mission[MAT][index][1] = "Terminer"
            break

    #Mettre a jour les data
    tf = open("Data\Mission.json", "w")
    json.dump (Mission, tf, sort_keys=True, indent=4)
    tf.close

    #fin de fonction
    print("Mission terminer, merci pour votre engagement.")
    Wait()
    ClearConsole()

#Fonction 4
def paraCouleur(Couleur, MAT):
    #Page de choix
    print("Choisir la couleur de votre interface parmi les suivant")
    print(
        f"\n{mycolor.W}1. Blanc"
        f"\n{mycolor.R}2. Rouge"
        f"\n{mycolor.G}3. Vert"
        f"\n{mycolor.O}4. Jaune"
        f"\n{mycolor.B}5. Bleu"
        f"\n{mycolor.P}6. Rose"
    )

    InterfaceColor(Couleur)

    #execution  du choix
    while True:
        choix = str(input("Choix: "))

        if choix == "1":
            Couleur = "W"
            break
        elif choix == "2":
            Couleur = "R"
            break
        elif choix == "3":
            Couleur = "G"
            break
        elif choix == "4":
            Couleur = "O"
            break
        elif choix == "5":
            Couleur = "B"
            break
        elif choix == "6":
            Couleur = "P"
            break
        else:
            ClearConsole()
            print(f"▓▓▓ Votre choix doit etre entre 1 et 6 ▓▓▓")
            
    
    #modification du parametre
    InterfaceColor(Couleur)

    #Enregistrement du parametre
    tf = open("Data\lstMat.json", "r")
    lst = json.load(tf, object_hook=dict)
    tf.close
    tf = open("Data\lstMat.json", "w")
    lst[MAT][1] = Couleur
    json.dump(lst, tf, sort_keys=True, indent=4)
    tf.close
