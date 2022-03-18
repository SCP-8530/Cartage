###########################################################################
### DEV: The_Am0nnal13
### Description du fichier: Liste de fonction et class qui gere l'interface graphique
###########################################################################

###################
### IMPORTATION ###
###################
import sys
from tkinter import Button
from PyQt5 import QtWidgets, QtCore
import code_interface_graphique

#####################################
### DECLARATION DE VALEUR GENERAL ###
#####################################
RECUPERATION_INPUT = ""

#################
### PROGRAMME ###
#################

###DEMARAGE DE LA FENETRE###
class fenetreQt(QtWidgets.QMainWindow, code_interface_graphique.Ui_MainWindow):
    """
    Class qui gere la form de mon interface
    :param parent: QtWidgets.QMainWindow et f.Ui_MainWindow
    """
    def __init__(self, parent=None):
        super(fenetreQt, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Systeme Cartage")

    
    def on_ValidationBtn_clicked(self): #attendre qu'un button soit activer
        ActifButton = False
        while ActifButton == False:
            if self.ValidationBtn.clicked():
                ActifButton == True

        texte = self.InputLineEdit.text()
        return texte

    def Modif_lbl(self, pMode="", pText=""): #ajouter du text au lbl
        if pMode == "add": #ajout du texte
            txtactuel = self.ConsoleLbl.Text()
            self.ConsoleLbl.setText(txtactuel + pText)
        elif pMode == "edit": #remplacer tout le texte du lbl
            self.ConsoleLbl.setText(pText)

def main():
    '''
    Fontion ayant comme but de demarer l'interface graphique
    '''
    app = QtWidgets.QApplication(sys.argv)
    form = fenetreQt()
    form.show()
    app.exec()

# ==Note Personnelle==
#----------
#| Nom des objet de l'interface graphique:
#|   le bouton = ValidationBtn
#|   l'entre de texte =  InputLineEdit
#|   le label = ConsoleLbl
#----------



