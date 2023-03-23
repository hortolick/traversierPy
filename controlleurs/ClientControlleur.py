from tkinter import *

from modeles.Client import Client
from vues.ClientsVue import ClientsVue
class ClientControlleur:
    def __init__(self, model, vue):
        self.model = model
        self.vue = vue
        self.vue.btnAjouter.config(command=lambda: self.creerClient())


    def remplirListeClients(self, clients):
        self.vue.lstClients.delete(0, END)
        for client in clients:
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
        print(self.model.nom, self.model.prenom, self.model.dateNaissance, self.model.adresse, self.model.ville, self.model.province, self.model.codePostal, self.model.telephone, self.model.courriel, self.model.numeroIdentification, self.model.sexe)

