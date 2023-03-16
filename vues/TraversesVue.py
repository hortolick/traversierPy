from tkinter import *

class VueTraverses(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Création d'un label numero traverse
        lblNoTraverse = Label(self, text="Numéro de traverse")
        lblNoTraverse.grid(column=0, row=0)

        # creation d'un champ de saisie numero traverse
        txtNoTraverse = Entry(self, width=40)
        txtNoTraverse.grid(column=1, row=0)

        # Création d'un label date hure
        lblDateHeure = Label(self, text="Date et heure")
        lblDateHeure.grid(column=0, row=1)

        # creation d'un champ de saisie date heure
        txtDateHeure = Entry(self, width=40)
        txtDateHeure.grid(column=1, row=1)

        # Création d'un label employe inscription
        lblEmployeInscription = Label(self, text="Employé inscription")
        lblEmployeInscription.grid(column=0, row=2)

        # creation d'une liste déroulante employe inscription
        txtEmployeInscription = Entry(self, width=40)
        txtEmployeInscription.grid(column=1, row=2)

        # Création d'une liste vehicule
        lstVehicule = Listbox(self, width=40)
        lstVehicule.grid(column=1, row=3)

        # création d'une liste client
        lstClient = Listbox(self, width=40)
        lstClient.grid(column=1, row=4)

        # Création d'un bouton ajouter
        btnAjouter = Button(self, text="Ajouter")
        btnAjouter.grid(column=0, row=4)
