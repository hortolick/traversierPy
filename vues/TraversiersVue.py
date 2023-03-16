from tkinter import *

class VueTraversiers(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Création d'un label Nom
        lblNom = Label(self, text="Nom")
        lblNom.grid(column=0, row=0)

        # creation d'un champ de saisie nom
        txtNom = Entry(self, width=40)
        txtNom.grid(column=1, row=0)

        # Création d'un label capacité vehicule
        lblCapaciteVehicule = Label(self, text="Capacité véhicule")
        lblCapaciteVehicule.grid(column=0, row=1)

        # creation d'un champ de saisie capacité vehicule
        txtCapaciteVehicule = Entry(self, width=40)
        txtCapaciteVehicule.grid(column=1, row=1)

        # Création d'un label capacité personne
        lblCapacitePersonne = Label(self, text="Capacité personne")
        lblCapacitePersonne.grid(column=0, row=2)

        # creation d'un champ de saisie capacité personne
        txtCapacitePersonne = Entry(self, width=40)
        txtCapacitePersonne.grid(column=1, row=2)

        # Création d'un label annee fabrication
        lblAnneeFabrication = Label(self, text="Année fabrication")
        lblAnneeFabrication.grid(column=0, row=3)

        # creation d'un champ de saisie annee fabrication
        txtAnneeFabrication = Entry(self, width=40)
        txtAnneeFabrication.grid(column=1, row=3)

        # Création d'un label date de mise en service
        lblDateMiseEnService = Label(self, text="Date de mise en service")
        lblDateMiseEnService.grid(column=0, row=4)

        # creation d'un champ de saisie date de mise en service
        txtDateMiseEnService = Entry(self, width=40)
        txtDateMiseEnService.grid(column=1, row=4)

        # Création d'un label liste employes
        lblListeEmployes = Label(self, text="Liste employés")
        lblListeEmployes.grid(column=0, row=5)

        # creation d'une liste employes
        txtListeEmployes = Entry(self, width=40)
        txtListeEmployes.grid(column=1, row=5)

        # Création d'un bouton ajouter
        btnAjouter = Button(self, text="Ajouter")
        btnAjouter.grid(column=0, row=6)
