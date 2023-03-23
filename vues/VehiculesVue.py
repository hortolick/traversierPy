from tkinter import *

class VehiculesVue(Frame):
    def __init__(self,master):
        # Création d'un label NoIdentification
        self.lblNoIdentification = Label(self, text="NoIdentification")
        self.lblNoIdentification.grid(column=0, row=0)

        # creation d'un champ de saisie NoIdentification
        self.txtNoIdentification = Entry(self, width=40)
        self.txtNoIdentification.grid(column=1, row=0)

        # Création d'un label Marque
        self.lblMarque = Label(self, text="Marque")
        self.lblMarque.grid(column=0, row=1)

        # creation d'un champ de saisie Marque
        self.txtMarque = Entry(self, width=40)
        self.txtMarque.grid(column=1, row=1)

        # Création d'un label Modèle
        self.lblModele = Label(self, text="Modèle")
        self.lblModele.grid(column=0, row=2)

        # creation d'un champ de saisie Modèle
        self.txtModele = Entry(self, width=40)
        self.txtModele.grid(column=1, row=2)

        # Création d'un label Année
        self.lblAnnee = Label(self, text="Année")
        self.lblAnnee.grid(column=0, row=3)

        # creation d'un champ de saisie Année
        self.txtAnnee = Entry(self, width=40)
        self.txtAnnee.grid(column=1, row=3)

        # Création d'un label Couleur
        self.lblCouleur = Label(self, text="Couleur")
        self.lblCouleur.grid(column=0, row=4)

        # creation d'un champ de saisie Couleur
        self.txtCouleur = Entry(self, width=40)
        self.txtCouleur.grid(column=1, row=4)

        # Création d'un label immatriculation
        self.lblImmatriculation = Label(self, text="Immatriculation")
        self.lblImmatriculation.grid(column=0, row=5)

        # creation d'un champ de saisie immatriculation
        self.txtImmatriculation = Entry(self, width=40)
        self.txtImmatriculation.grid(column=1, row=5)

        # Création d'un bouton Ajouter
        self.btnAjouter = Button(self, text="Ajouter")
        self.btnAjouter.grid(column=0, row=6)
