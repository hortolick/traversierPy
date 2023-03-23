from tkinter import *

from modeles.Client import Client
from vues.ClientsVue import ClientsVue
class ClientControlleur:

    def creerClient(self):
        print("hewegoooo")
        self.model.nom = self.vue.txtNom.get()
        self.model.adresse = self.vue.txtAdresse.get()
        self.model.ville = self.vue.txtVille.get()
        self.model.province = self.vue.txtProvince.get()
        self.model.codePostal = self.vue.txtCodePostal.get()
        self.model.telephone = self.vue.txtTelephone.get()
        self.model.courriel = self.vue.txtCourriel.get()
        self.model.numeroIdentification = self.vue.txtNumeroIdentification.get()
        self.model.sexe = self.vue.txtSexe.get()
        self.model.dateNaissance = self.vue.txtDateNaissance.get()
        print(self.model)
    def __init__(self, model, vue):

        self.model = model
        self.vue = vue
        print(type(self.vue.btnAjouter))
        self.vue.btnAjouter.config(command=lambda: self.creerClient())

