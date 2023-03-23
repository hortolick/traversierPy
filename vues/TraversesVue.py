from tkinter import *

class TraversesVue(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Création d'un label numero traverse
        self.lblNoTraverse = Label(self, text="Numéro de traverse")
        self.lblNoTraverse.grid(column=0, row=0)

        # creation d'un champ de saisie numero traverse
        self.txtNoTraverse = Entry(self, width=40)
        self.txtNoTraverse.grid(column=1, row=0)

        # Création d'un label date hure
        self.lblDateHeure = Label(self, text="Date et heure")
        self.lblDateHeure.grid(column=0, row=1)

        # creation d'un champ de saisie date heure
        self.txtDateHeure = Entry(self, width=40)
        self.txtDateHeure.grid(column=1, row=1)

        # Création d'un label employe inscription
        self.lblEmployeInscription = Label(self, text="Employé inscription")
        self.lblEmployeInscription.grid(column=0, row=2)

        # Création de variables pour la liste deroulante
        self.selection = StringVar()
        self.selection.set("Employé inscription")

        self.listeEmployes = ["Employé inscription", "Employé 1", "Employé 2", "Employé 3"]

        # creation d'une liste déroulante employe inscription
        self.dropEmployeInscription = OptionMenu(self, self.selection, *self.listeEmployes)
        self.dropEmployeInscription.grid(column=1, row=2)

        # Création d'une liste vehicule
        self.lstVehicule = Listbox(self, width=40)
        self.lstVehicule.grid(column=1, row=3)

        # création d'une liste client
        self.lstClient = Listbox(self, width=40)
        self.lstClient.grid(column=1, row=4)


        # Création d'un bouton ajouter
        self.btnCreer = Button(self, text="Creer")
        self.btnCreer.grid(column=0, row=4)


