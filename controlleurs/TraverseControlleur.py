from tkinter import *
import xml.etree.ElementTree as ET
from modeles.Traverse import Traverse
from vues.TraversesVue import TraversesVue

class TraverseControlleur:
    def __init__(self, model, vue):
        self.model = model
        self.vue = vue

        self.vue.btnCalculerRevenu.config(command=lambda: self.calculerPrix())

        self.nbrClients = 0
        self.nbrVehicules = 0

        self.xmlroot = ET.parse("TransStLaurent.xml")

    def obtenirNombres(self):
        self.nbrClients = len(self.xmlroot.getroot().find("clients").findall("client"))
        self.nbrVeicules = len(self.xmlroot.getroot().find("vehicules").findall("vehicule"))

        self.vue.txtNbrClients.insert(0, self.nbrClients)
        self.vue.txtNbrVehicules.insert(0, self.nbrVehicules)

    def calculerPrix(self):
        prixPersonne = int(self.vue.txtPrixParPersonne.get()) * int(self.vue.txtNbrClients.get())
        prixVehicule = int(self.vue.txtPrixParVehicule.get()) * int(self.vue.txtNbrVehicules.get())

        self.vue.lblRevenuClients.config(text="Revenu clients: "+str(prixPersonne))
        self.vue.lblRevenuVehicules.config(text="Revenu véhicules: "+str(prixVehicule))
        self.vue.lblRevenuTotal.config(text="Revenu total: "+str((prixPersonne + prixVehicule)))
        print("Revenu clients: "+str(prixPersonne) + " Revenu véhicules: "+str(prixVehicule) + " Revenu total: "+str((prixPersonne + prixVehicule)))