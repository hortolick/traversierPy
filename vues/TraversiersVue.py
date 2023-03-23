from tkinter import *

class TraversiersVue(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Création d'un label Nom
        self.lblNom = Label(self, text="Nom")
        self.lblNom.grid(column=0, row=0)

        # creation d'un champ de saisie nom
        self.txtNom = Entry(self, width=40)
        self.txtNom.grid(column=1, row=0)

        # Création d'un label capacité vehicule
        self.lblCapaciteVehicule = Label(self, text="Capacité véhicule")
        self.lblCapaciteVehicule.grid(column=0, row=1)

        # creation d'un champ de saisie capacité vehicule
        self.txtCapaciteVehicule = Entry(self, width=40)
        self.txtCapaciteVehicule.grid(column=1, row=1)

        # Création d'un label capacité personne
        self.lblCapacitePersonne = Label(self, text="Capacité personne")
        self.lblCapacitePersonne.grid(column=0, row=2)

        # creation d'un champ de saisie capacité personne
        self.txtCapacitePersonne = Entry(self, width=40)
        self.txtCapacitePersonne.grid(column=1, row=2)

        # Création d'un label annee fabrication
        self.lblAnneeFabrication = Label(self, text="Année fabrication")
        self.lblAnneeFabrication.grid(column=0, row=3)

        # creation d'un champ de saisie annee fabrication
        self.txtAnneeFabrication = Entry(self, width=40)
        self.txtAnneeFabrication.grid(column=1, row=3)

        # Création d'un label date de mise en service
        self.lblDateMiseEnService = Label(self, text="Date de mise en service")
        self.lblDateMiseEnService.grid(column=0, row=4)

        # creation d'un champ de saisie date de mise en service
        self.txtDateMiseEnService = Entry(self, width=40)
        self.txtDateMiseEnService.grid(column=1, row=4)

        # Création d'un label liste employes
        self.lblListeEmployes = Label(self, text="Liste employés")
        self.lblListeEmployes.grid(column=0, row=5)

        # creation d'une liste employes
        self.txtListeEmployes = Entry(self, width=40)
        self.txtListeEmployes.grid(column=1, row=5)

        # Création d'un bouton ajouter
        self.btnAjouter = Button(self, text="Ajouter")
        self.btnAjouter.grid(column=0, row=6)
