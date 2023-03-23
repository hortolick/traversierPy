from tkinter import *

class EmployesVue(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Création d'un label Nom
        self.lblNom = Label(self, text="Nom")
        self.lblNom.grid(column=0, row=0)

        # creation d'un champ de saisie nom
        self.txtNom = Entry(self, width=40)
        self.txtNom.grid(column=1, row=0)

        # Création d'un label Prénom
        self.lblPrenom = Label(self, text="Prénom")
        self.lblPrenom.grid(column=0, row=1)

        # creation d'un champ de saisie prénom
        self.txtPrenom = Entry(self, width=40)
        self.txtPrenom.grid(column=1, row=1)

        # Création d'un label adresse
        self.lblAdresse = Label(self, text="Adresse")
        self.lblAdresse.grid(column=0, row=2)

        # creation d'un champ de saisie adresse
        self.txtAdresse = Entry(self, width=40)
        self.txtAdresse.grid(column=1, row=2)

        # Création d'un label ville
        self.lblVille = Label(self, text="Ville")
        self.lblVille.grid(column=0, row=3)

        # creation d'un champ de saisie ville
        self.txtVille = Entry(self, width=40)
        self.txtVille.grid(column=1, row=3)

        # Création d'un label province
        self.lblProvince = Label(self, text="Province")
        self.lblProvince.grid(column=0, row=4)

        # creation d'un champ de saisie province
        self.txtProvince = Entry(self, width=40)
        self.txtProvince.grid(column=1, row=4)

        # Création d'un label code postal
        self.lblCodePostal = Label(self, text="Code postal")
        self.lblCodePostal.grid(column=0, row=5)

        # creation d'un champ de saisie code postal
        self.txtCodePostal = Entry(self, width=40)
        self.txtCodePostal.grid(column=1, row=5)

        # Création d'un label téléphone
        self.lblTelephone = Label(self, text="Téléphone")
        self.lblTelephone.grid(column=0, row=6)

        # creation d'un champ de saisie téléphone
        self.txtTelephone = Entry(self, width=40)
        self.txtTelephone.grid(column=1, row=6)

        # Création d'un label courriel
        self.lblCourriel = Label(self, text="Courriel")
        self.lblCourriel.grid(column=0, row=7)

        # creation d'un champ de saisie courriel
        self.txtCourriel = Entry(self, width=40)
        self.txtCourriel.grid(column=1, row=7)

        #creation d'un label numero d'emplye
        self.lblNoEmploye = Label(self, text="Numéro d'employé")
        self.lblNoEmploye.grid(column=0, row=8)

        #creation d'un champ de saisie numero d'employe
        self.txtNoEmploye = Entry(self, width=40)
        self.txtNoEmploye.grid(column=1, row=8)

        #creation d'un label numero d'assurance sociale
        self.lblNAS = Label(self, text="Numéro d'assurance sociale")
        self.lblNAS.grid(column=0, row=9)

        #creation d'un champ de saisie numero d'assurance sociale
        self.txtNAS = Entry(self, width=40)
        self.txtNAS.grid(column=1, row=9)

        #creation d'un label date d'embauche
        self.lblDateEmbauche = Label(self, text="Date d'embauche")
        self.lblDateEmbauche.grid(column=0, row=10)

        #creation d'un champ de saisie date d'embauche
        self.txtDateEmbauche = Entry(self, width=40)
        self.txtDateEmbauche.grid(column=1, row=10)

        #creation d'un label date d'arret
        self.lblDateArret = Label(self, text="Date d'arret")
        self.lblDateArret.grid(column=0, row=11)

        #creation d'un champ de saisie date d'arret
        self.txtDateArret = Entry(self, width=40)
        self.txtDateArret.grid(column=1, row=11)


        #creation d'un bouton ajouter
        self.btnAjouter = Button(self, text="Ajouter")
        self.btnAjouter.grid(column=0, row=12)

        #creation d'une liste d'employes
        self.lstEmployes = Listbox(self, width=40)
        self.lstEmployes.grid(column=1, row=12)