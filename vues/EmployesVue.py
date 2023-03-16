from tkinter import *

class EmployesVue(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Création d'un label Nom
        lblNom = Label(self, text="Nom")
        lblNom.grid(column=0, row=0)

        # creation d'un champ de saisie nom
        txtNom = Entry(self, width=40)
        txtNom.grid(column=1, row=0)

        # Création d'un label Prénom
        lblPrenom = Label(self, text="Prénom")
        lblPrenom.grid(column=0, row=1)

        # creation d'un champ de saisie prénom
        txtPrenom = Entry(self, width=40)
        txtPrenom.grid(column=1, row=1)

        # Création d'un label adresse
        lblAdresse = Label(self, text="Adresse")
        lblAdresse.grid(column=0, row=2)

        # creation d'un champ de saisie adresse
        txtAdresse = Entry(self, width=40)
        txtAdresse.grid(column=1, row=2)

        # Création d'un label ville
        lblVille = Label(self, text="Ville")
        lblVille.grid(column=0, row=3)

        # creation d'un champ de saisie ville
        txtVille = Entry(self, width=40)
        txtVille.grid(column=1, row=3)

        # Création d'un label province
        lblProvince = Label(self, text="Province")
        lblProvince.grid(column=0, row=4)

        # creation d'un champ de saisie province
        txtProvince = Entry(self, width=40)
        txtProvince.grid(column=1, row=4)

        # Création d'un label code postal
        lblCodePostal = Label(self, text="Code postal")
        lblCodePostal.grid(column=0, row=5)

        # creation d'un champ de saisie code postal
        txtCodePostal = Entry(self, width=40)
        txtCodePostal.grid(column=1, row=5)

        # Création d'un label téléphone
        lblTelephone = Label(self, text="Téléphone")
        lblTelephone.grid(column=0, row=6)

        # creation d'un champ de saisie téléphone
        txtTelephone = Entry(self, width=40)
        txtTelephone.grid(column=1, row=6)

        # Création d'un label courriel
        lblCourriel = Label(self, text="Courriel")
        lblCourriel.grid(column=0, row=7)

        # creation d'un champ de saisie courriel
        txtCourriel = Entry(self, width=40)
        txtCourriel.grid(column=1, row=7)

        #creation d'un label numero d'emplye
        lblNoEmploye = Label(self, text="Numéro d'employé")
        lblNoEmploye.grid(column=0, row=8)

        #creation d'un champ de saisie numero d'employe
        txtNoEmploye = Entry(self, width=40)
        txtNoEmploye.grid(column=1, row=8)

        #creation d'un label numero d'assurance sociale
        lblNAS = Label(self, text="Numéro d'assurance sociale")
        lblNAS.grid(column=0, row=9)

        #creation d'un champ de saisie numero d'assurance sociale
        txtNAS = Entry(self, width=40)
        txtNAS.grid(column=1, row=9)

        #creation d'un label date d'embauche
        lblDateEmbauche = Label(self, text="Date d'embauche")
        lblDateEmbauche.grid(column=0, row=10)

        #creation d'un champ de saisie date d'embauche
        txtDateEmbauche = Entry(self, width=40)
        txtDateEmbauche.grid(column=1, row=10)

        #creation d'un label date d'arret
        lblDateArret = Label(self, text="Date d'arret")
        lblDateArret.grid(column=0, row=11)

        #creation d'un champ de saisie date d'arret
        txtDateArret = Entry(self, width=40)
        txtDateArret.grid(column=1, row=11)

        def ajouterEmploye():
            lstEmployes.insert(END, txtNom.get() + " " + txtPrenom.get())

        #creation d'un bouton ajouter
        btnAjouter = Button(self, text="Ajouter", command=ajouterEmploye)
        btnAjouter.grid(column=0, row=12)

        #creation d'une liste d'employes
        lstEmployes = Listbox(self, width=40)
        lstEmployes.grid(column=1, row=12)