from tkinter import *
import xml.etree.ElementTree as ET
from modeles.Vehicule import Vehicule

class VehiculeControlleur:
    def __init__(self, model, vue):
        self.model = model
        self.vue = vue
        self.vue.btnAjouter.config(command=lambda: self.creerVehicule())

        self.listeVehicules = []
        self.xmlroot = ET.parse("TransStLaurent.xml")

    def remplirListeVehicules(self):
        for vehiculexml in self.xmlroot.getroot().find("vehicules").findall("vehicule"):
            vehicule_attrs = {}
            for attr in vehiculexml.attrib:
                vehicule_attrs[attr] = vehiculexml.get(attr)
            vehicule = Vehicule(**vehicule_attrs)
            self.listeVehicules.append(vehicule)

        self.vue.lstVehicules.delete(0, END)
        for vehicule in self.listeVehicules:
            self.vue.lstVehicules.insert(END, vehicule.noIdentification + " " + vehicule.marque + " " + vehicule.modele)


    def creerVehicule(self):
        self.model.noIdentification = self.vue.txtNoIdentification.get()
        self.model.marque = self.vue.txtMarque.get()
        self.model.modele = self.vue.txtModele.get()
        self.model.couleur = self.vue.txtCouleur.get()
        self.model.annee = self.vue.txtAnnee.get()
        self.model.immatriculation = self.vue.txtImmatriculation.get()

        vehicule_elem = ET.SubElement(self.xmlroot.getroot().find("vehicules"), "vehicule")
        vehicule_elem.set("noIdentification", self.model.noIdentification)
        vehicule_elem.set("marque", self.model.marque)
        vehicule_elem.set("modele", self.model.modele)
        vehicule_elem.set("couleur", self.model.couleur)
        vehicule_elem.set("annee", self.model.annee)
        vehicule_elem.set("immatriculation", self.model.immatriculation)

        self.xmlroot.write("TransStLaurent.xml")
        self.vue.lstVehicules.insert(END, self.model.noIdentification + " " + self.model.marque + " " + self.model.modele)
        self.viderChamps()

    def viderChamps(self):
        self.vue.txtNoIdentification.delete(0, END)
        self.vue.txtMarque.delete(0, END)
        self.vue.txtModele.delete(0, END)
        self.vue.txtCouleur.delete(0, END)
        self.vue.txtAnnee.delete(0, END)
        self.vue.txtImmatriculation.delete(0, END)