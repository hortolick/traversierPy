from tkinter import *
from tkinter import ttk

import xml.etree.ElementTree as ET

from modeles.Client import Client
from modeles.Employe import Employe
from modeles.Vehicule import Vehicule
# from modeles.Traversier import Traversier
from modeles.Traverse import Traverse
from vues.TransStLaurent import TransStLaurentVue
from controlleurs.ClientControlleur import ClientControlleur
from controlleurs.EmployeControlleur import EmployeControlleur
from controlleurs.VehiculeControlleur import VehiculeControlleur
from controlleurs.TraverseControlleur import TraverseControlleur
vehicules = []
traversiers = []
traverses = []

xmlroot = ET.parse("TransStLaurent.xml").getroot()

window = Tk()
window.title("Transport St-Laurent")
window.geometry("640x480")

# Création d'un controleur de tab
tabControl = TransStLaurentVue(window)
tabControl.pack(expand=1, fill="both")
#client = Client()
clientControlleur = ClientControlleur(Client, tabControl.tabClients)
clientControlleur.remplirListeClients()

employeControlleur = EmployeControlleur(Employe, tabControl.tabEmployes)
employeControlleur.remplirListeEmployes()

vehiculeControlleur = VehiculeControlleur(Vehicule, tabControl.tabVehicules)
vehiculeControlleur.remplirListeVehicules()

traverseControlleur = TraverseControlleur(Traverse, tabControl.tabTraverse)
traverseControlleur.obtenirNombres()
#traverseControlleur.calculerPrix()

window.mainloop()