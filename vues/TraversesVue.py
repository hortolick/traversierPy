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

        # creation d'une liste déroulante employe inscription
        #self.dropEmployeInscription = OptionMenu(self)
        #self.dropEmployeInscription.grid(column=1, row=2)

        # creation d'un label nombre clients
        self.lblNbClients = Label(self, text="Nombre de clients")
        self.lblNbClients.grid(column=0, row=3)

        # creation d'un champ de saisie nombre clients
        self.txtNbrClients = Entry(self, width=40)
        self.txtNbrClients.grid(column=1, row=3)

        # creation d'un label nombre vehicules
        self.lblNbrVehicules = Label(self, text="Nombre de véhicules")
        self.lblNbrVehicules.grid(column=0, row=4)

        # creation d'un champ de saisie nombre vehicules
        self.txtNbrVehicules = Entry(self, width=40)
        self.txtNbrVehicules.grid(column=1, row=4)

        # creation d'un label prix par personne
        self.lblPrixParPersonne = Label(self, text="Prix par personne")
        self.lblPrixParPersonne.grid(column=2, row=3)

        # creation d'un champ de saisie prix par personne
        self.txtPrixParPersonne = Entry(self, width=40)
        self.txtPrixParPersonne.grid(column=3, row=3)

        # creation d'un label prix par vehicule
        self.lblPrixParVehicule = Label(self, text="Prix par véhicule")
        self.lblPrixParVehicule.grid(column=2, row=4)

        # creation d'un champ de saisie prix par vehicule
        self.txtPrixParVehicule = Entry(self, width=40)
        self.txtPrixParVehicule.grid(column=3, row=4)

        # creation d'un label revenu clients
        self.lblRevenuClients = Label(self, text="Revenu clients")
        self.lblRevenuClients.grid(column=0, row=5)

        # creation d'un label revenu vehicules
        self.lblRevenuVehicules = Label(self, text="Revenu véhicules")
        self.lblRevenuVehicules.grid(column=0, row=6)

        # creation d'un label revenu total
        self.lblRevenuTotal = Label(self, text="Revenu total")
        self.lblRevenuTotal.grid(column=0, row=7)

        # creation d'un bouton calculer revenu
        self.btnCalculerRevenu = Button(self, text="Calculer revenu")
        self.btnCalculerRevenu.grid(column=1, row=8)
