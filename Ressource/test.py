###########################################################################
### DEV: The_Am0nnal13
### Description du fichier: fichier de test en dehors du programme
###########################################################################

###################
### IMPORTATION ###
###################
#importation projet
import code_interface_graphique
#importation python
import sys
from PyQt5 import QtWidgets

###############################################
### DEFINITION DES FONCTIONS ET DES CLASSES ###
###############################################
class fenetreQt(QtWidgets.QMainWindow, code_interface_graphique.Ui_MainWindow):
    """
    Class qui gere la form de mon interface
    :param parent: QtWidgets.QMainWindow et f.Ui_MainWindow
    """
    def __init__(self, parent=None):
        super(fenetreQt, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Systeme Cartage")

def main():
    '''
    Fontion ayant comme but de demarer l'interface graphique
    '''
    app = QtWidgets.QApplication(sys.argv)
    form = fenetreQt()
    form.show()
    app.exec()

#################
### PROGRAMME ###
#################
#demarrage de l'interface graphique
if __name__ == "__main__":
    main()