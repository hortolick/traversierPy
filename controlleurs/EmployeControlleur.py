from tkinter import *
import xml.etree.ElementTree as ET
from modeles.Employe import Employe


class EmployeControlleur:
    def __init__(self, model, vue):
        self.model = model
        self.vue = vue
        self.vue.btnAjouter.config(command=lambda: self.creerEmploye())

        self.listeEmployes = []
        self.xmlroot = ET.parse("TransStLaurent.xml")

    def remplirListeEmployes(self):
        for employexml in self.xmlroot.getroot().find("employes").findall("employe"):
            employe_attrs = {}
            for attr in employexml.attrib:
                employe_attrs[attr] = employexml.get(attr)
            employe = Employe(**employe_attrs)
            self.listeEmployes.append(employe)

        self.vue.lstEmployes.delete(0, END)
        for employe in self.listeEmployes:
            self.vue.lstEmployes.insert(END, employe.nom + " " + employe.prenom)


    def creerEmploye(self):
        self.model.nom = self.vue.txtNom.get()
        self.model.prenom = self.vue.txtPrenom.get()
        self.model.adresse = self.vue.txtAdresse.get()
        self.model.ville = self.vue.txtVille.get()
        self.model.province = self.vue.txtProvince.get()
        self.model.codePostal = self.vue.txtCodePostal.get()
        self.model.telephone = self.vue.txtTelephone.get()
        self.model.courriel = self.vue.txtCourriel.get()
        self.model.noEmploye = self.vue.txtNoEmploye.get()
        self.model.nAS = self.vue.txtNAS.get()
        self.model.dateEmbauche = self.vue.txtDateEmbauche.get()
        self.model.dateArret = self.vue.txtDateArret.get()

        employe_elem = ET.SubElement(self.xmlroot.getroot().find("employes"), "employe")
        employe_elem.set("nom", self.model.nom)
        employe_elem.set("prenom", self.model.prenom)
        employe_elem.set("adresse", self.model.adresse)
        employe_elem.set("ville", self.model.ville)
        employe_elem.set("province", self.model.province)
        employe_elem.set("codePostal", self.model.codePostal)
        employe_elem.set("telephone", self.model.telephone)
        employe_elem.set("courriel", self.model.courriel)
        employe_elem.set("noEmploye", self.model.noEmploye)
        employe_elem.set("nAS", self.model.nAS)
        employe_elem.set("dateEmbauche", self.model.dateEmbauche)
        employe_elem.set("dateArret", self.model.dateArret)

        self.xmlroot.write("TransStLaurent.xml")
        self.vue.lstEmployes.insert(END, self.model.nom + " " + self.model.prenom)

        self.viderChanmps()


    def viderChanmps(self):
        self.vue.txtNom.delete(0, END)
        self.vue.txtPrenom.delete(0, END)
        self.vue.txtAdresse.delete(0, END)
        self.vue.txtVille.delete(0, END)
        self.vue.txtProvince.delete(0, END)
        self.vue.txtCodePostal.delete(0, END)
        self.vue.txtTelephone.delete(0, END)
        self.vue.txtCourriel.delete(0, END)
        self.vue.txtNoEmploye.delete(0, END)
        self.vue.txtNAS.delete(0, END)
        self.vue.txtDateEmbauche.delete(0, END)
        self.vue.txtDateArret.delete(0, END)

        self.vue.txtNom.focus()