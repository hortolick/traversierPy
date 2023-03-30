from tkinter import *
import xml.etree.ElementTree as ET
from modeles.Client import Client
from vues.ClientsVue import ClientsVue
class ClientControlleur:
    def __init__(self, model, vue):
        self.model = model
        self.vue = vue
        self.vue.btnAjouter.config(command=lambda: self.creerClient())

        self.listeClients=[]
        self.xmlroot = ET.parse("TransStLaurent.xml")

    def remplirListeClients(self):

        for clientxml in self.xmlroot.getroot().find("clients").findall("client"):
            client_attrs = {}
            for attr in clientxml.attrib:
                client_attrs[attr] = clientxml.get(attr)
            client = Client(**client_attrs)
            self.listeClients.append(client)

        self.vue.lstClients.delete(0, END)
        for client in self.listeClients:
            self.vue.lstClients.insert(END, client.nom + " " + client.prenom)

    def creerClient(self):
        self.model.nom = self.vue.txtNom.get()
        self.model.prenom = self.vue.txtPrenom.get()
        self.model.dateNaissance = self.vue.txtDateNaissance.get()
        self.model.adresse = self.vue.txtAdresse.get()
        self.model.ville = self.vue.txtVille.get()
        self.model.province = self.vue.txtProvince.get()
        self.model.codePostal = self.vue.txtCodePostal.get()
        self.model.telephone = self.vue.txtTelephone.get()
        self.model.courriel = self.vue.txtCourriel.get()
        self.model.numeroIdentification = self.vue.txtNumeroIdentification.get()
        self.model.sexe = self.vue.txtSexe.get()

        client_elem = ET.SubElement(self.xmlroot.getroot().find("clients"), "client")
        client_elem.set("nom", self.model.nom)
        client_elem.set("prenom", self.model.prenom)
        client_elem.set("dateNaissance", self.model.dateNaissance)
        client_elem.set("adresse", self.model.adresse)
        client_elem.set("ville", self.model.ville)
        client_elem.set("province", self.model.province)
        client_elem.set("codePostal", self.model.codePostal)
        client_elem.set("telephone", self.model.telephone)
        client_elem.set("courriel", self.model.courriel)
        client_elem.set("numeroIdentification", self.model.numeroIdentification)
        client_elem.set("sexe", self.model.sexe)


        self.xmlroot.write("TransStLaurent.xml")
        self.vue.lstClients.insert(END, self.model.nom + " " + self.model.prenom)
        self.viderChamps()


    def viderChamps(self):
        self.vue.txtNom.delete(0, END)
        self.vue.txtPrenom.delete(0, END)
        self.vue.txtDateNaissance.delete(0, END)
        self.vue.txtAdresse.delete(0, END)
        self.vue.txtVille.delete(0, END)
        self.vue.txtProvince.delete(0, END)
        self.vue.txtCodePostal.delete(0, END)
        self.vue.txtTelephone.delete(0, END)
        self.vue.txtCourriel.delete(0, END)
        self.vue.txtNumeroIdentification.delete(0, END)
        self.vue.txtSexe.delete(0, END)

        self.vue.txtNom.focus()
