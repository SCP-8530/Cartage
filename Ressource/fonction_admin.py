###########################################################################
### DEV: The_Am0nnal13
### Description du fichier: Liste des fonction utiliser dans l'interface admin
###########################################################################

###################
### IMPORTATION ###
###################
import json
from universal_fonction import *
 
#################
### PROGRAMME ###
#################
#fonction 1
def AjoutCR(Matricule) :
    #Recuperation des informations du crystalien
    Nom = str(input("Entré le prenom du crystalien: "))
    Role = str(input("Entré le role du crystalien: "))
    Renumeration = str(input("Entré la rénumeration du crystalien: "))

    # Ajout des Datas
    tf = open("Data\lstCrystalien.json", "r")
    RR = json.load(tf, object_hook=dict)
    tf.close
    tf = open("Data\lstCrystalien.json", "w")
    RR[Matricule] = {}
    RR[Matricule]["Prenom"] = f"{Nom}"
    RR[Matricule]["Nom"] = "De Langitia"
    RR[Matricule]["Fonction"] = f"{Role}"
    RR[Matricule]["Renumeration"] = f"{Renumeration}"
    json.dump(RR, tf, sort_keys=True, indent=4)
    tf.close()

    #Ajout de la connection
    tfr = open("Data\lstMat.json", "r")
    MAT = json.load(tfr, object_hook=dict)
    tfr.close
    MAT[Matricule] = ["U","O"]
    tfw = open("Data\lstMat.json", "w")
    json.dump(MAT, tfw, sort_keys=True, indent=4)
    tfw.close

    #fin de la fonction
    ClearConsole()
    print(f"{mycolor.G}Matricule enregistrer")
    
#fonction 2
def AfficherLstCR() :
    #recuperation des données
    tf = open("Data\lstCrystalien.json", "r")
    RR = json.load(tf, object_hook=dict)
    tf.close

    #afficher les données
    ##entete
    entete = ["Matricule", "Fonction", "Identiter", "Revenue"]
    print(f"{mycolor.O}" + "*" * 64)
    print(f"*{entete[0]:<10}*{entete[2]:^40}*{entete[3]:>10}*\n*{entete[1]:^62}*")
    print("#" * 64 + f"{mycolor.W}")
    ##donner principal
    for Matricule in RR:
        Fonction = RR[Matricule]["Fonction"]
        Identiter = RR[Matricule]["Prenom"] + " " + RR[Matricule]["Nom"]
        Revenue = RR[Matricule]["Renumeration"]
        print(f"*{Matricule:<10}*{Identiter:^40}*{Revenue:>10}*\n*{Fonction:^62}*")
        print(f"{mycolor.O}" + "*" * 64 + f"{mycolor.W}")
    
    #fin de la fonction
    Wait()
    ClearConsole()

#fonction 3
def ModifCR(RR, Matricule):
    #Choix de la modif
    while True:
        print(f"Que souhaitez vous modifiez?\n1. Prenom\n2. Nom\n3. Fonction\n4. Renumeration")
        choix = input(">>> ")
        
        #modification
        if choix == 1:
            data = RR[Matricule]["Prenom"]
            print(f"Le Prenom du matricule est {data}")
            newData = input("Donner le nouveau Prenom: ")

            #enregistrer les donner modifier
            tf = open("Data\lstCrystalien.json", "w")
            data = newData
            json.dump(RR, tf, sort_keys=True, indent=4)
            tf.close

            #fin de fonction
            ClearConsole()
            print(f"{mycolor.G}Modification fait")
            break
        elif choix == 2:
            data = RR[Matricule]["Nom"]
            print(f"Le Nom du matricule est {data}")
            newData = input("Donner le nouveau Nom: ")

            #enregistrer les donner modifier
            tf = open("Data\lstCrystalien.json", "w")
            data = newData
            json.dump(RR, tf, sort_keys=True, indent=4)
            tf.close

            #fin de fonction
            ClearConsole()
            print(f"{mycolor.G}Modification fait")
            break
        elif choix == 3:
            data = RR[Matricule]["Fonction"]
            print(f"La Fonction du matricule est {data}")
            newData = input("Donner la nouvelle Fonction: ")

            #enregistrer les donner modifier
            tf = open("Data\lstCrystalien.json", "w")
            data = newData
            json.dump(RR, tf, sort_keys=True, indent=4)
            tf.close

            #fin de fonction
            ClearConsole()
            print(f"{mycolor.G}Modification fait")
            break
        elif choix == 4:
            data = RR[Matricule]["Renumeration"]
            print(f"La Renumeration du matricule est {data}")
            newData = input("Donner la nouvelle Renumeration: ")

            #enregistrer les donner modifier
            tf = open("Data\lstCrystalien.json", "w")
            data = newData
            json.dump(RR, tf, sort_keys=True, indent=4)
            tf.close

            #fin de fonction
            ClearConsole()
            print(f"{mycolor.G}Modification fait")
            break
        else:
            print(f"{mycolor.R}Option non valide{mycolor.W}")

#fonction 4
def SupprCR(Matricule):
    # Verification de la suppression
    while True:
        YN = str(input("Etes-vous bien sur de supprimer les informations du crystalien? (Y ou N) "))

        if YN == "n" or YN == "N":
            print(f"{mycolor.R}")
            break
        elif YN == "y" or YN == "Y":

            # Supprimer des datas
            tf = open("Data\lstCrystalien.json", "r")
            RR = json.load(tf, object_hook=dict)
            tf.close
            tf = open("Data\lstCrystalien.json", "w")
            del RR[Matricule]
            json.dump(RR, tf, sort_keys=True, indent=4)
            tf.close()

            # Supprimer la connection
            tfr = open("Data\lstMat.json", "r")
            MAT = json.load(tfr, object_hook=dict)
            tfr.close
            del MAT[Matricule]
            tfw = open("Data\lstMat.json", "w")
            json.dump(MAT, tfw, sort_keys=True, indent=4)
            tfw.close

            #fin de fonction
            ClearConsole()
            print(f"{mycolor.G}Matricule supprimer")
            break

        else:
            print(f"{mycolor.R}Y = oui et N = non{mycolor.W}")

#fonction 5
def AjoutMission(Matricule):
    #recupere les details de la mission
    Detail = str(input("Veuiller donner les detail de la mission (eviter des missions trop longue): "))
    tf = open("Data\Mission.json", "r")
    Nmission = json.load(tf, object_hook=dict)
    Nombre = int(Nmission["missionN"]) + 1
    tf.close

    #Ajout dans la liste
    Nmission[Matricule] = []
    Nmission[Matricule].append([Nombre,"Non-debuter",Detail])
    Nmission["missionN"] = str(Nombre)
    tf = open("Data\Mission.json", "w")
    json.dump(Nmission, tf, sort_keys=True, indent=4)
    tf.close

    #fin de fonction
    ClearConsole()
    print(f"{mycolor.G}La mission a bien ete ajouter.")
    

#fonction 6
def AfficherMission():
    #recupere les datas
    tf = open("Data\Mission.json", "r")
    Mission = json.load(tf, object_hook=dict)
    tf.close

    #Affichage des datas
    for cle in Mission.keys():
        if cle != "missionN":
            startlst = f"---Les missions de {cle}---"
            print(f"\n{startlst:^100}")
            print(f"{mycolor.O}*{mycolor.W}" * 100)
            for index in range(0, len(Mission[cle]), 1):
                #recuperation des divers valeur de l'index
                info1 = f"ID de mission: {Mission[cle][index][0]}"
                info2 = f"Etat de la mission: {Mission[cle][index][1]}"
                info3 = f"Detail de la mission: {Mission[cle][index][2]}"
                #affichage de ses valeurs
                print(f"{info1:<50}{info2:>50}\n{info3:<100}")
                print(f"{mycolor.O}#{mycolor.W}" * 100)
    

    #fin de fonction
    Wait()
    ClearConsole()
