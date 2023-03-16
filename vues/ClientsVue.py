from tkinter import *

class ClientsVue(Frame):
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

        #cretion d'un label Date de naissance
        lblDateNaissance = Label(self, text="Date de naissance")
        lblDateNaissance.grid(column=0, row=2)

        #creation d'un champ de saisie date de naissance
        txtDateNaissance = Entry(self, width=40)
        txtDateNaissance.grid(column=1, row=2)

        # Création d'un label adresse
        lblAdresse = Label(self, text="Adresse")
        lblAdresse.grid(column=0, row=3)

        # creation d'un champ de saisie adresse
        txtAdresse = Entry(self, width=40)
        txtAdresse.grid(column=1, row=3)

        # Création d'un label ville
        lblVille = Label(self, text="Ville")
        lblVille.grid(column=0, row=4)

        # creation d'un champ de saisie ville
        txtVille = Entry(self, width=40)
        txtVille.grid(column=1, row=4)

        # Création d'un label province
        lblProvince = Label(self, text="Province")
        lblProvince.grid(column=0, row=5)

        # creation d'un champ de saisie province
        txtProvince = Entry(self, width=40)
        txtProvince.grid(column=1, row=5)

        # Création d'un label code postal
        lblCodePostal = Label(self, text="Code postal")
        lblCodePostal.grid(column=0, row=6)

        # creation d'un champ de saisie code postal
        txtCodePostal = Entry(self, width=40)
        txtCodePostal.grid(column=1, row=6)

        # Création d'un label téléphone
        lblTelephone = Label(self, text="Téléphone")
        lblTelephone.grid(column=0, row=7)

        # creation d'un champ de saisie téléphone
        txtTelephone = Entry(self, width=40)
        txtTelephone.grid(column=1, row=7)

        # Création d'un label courriel
        lblCourriel = Label(self, text="Courriel")
        lblCourriel.grid(column=0, row=8)

        # creation d'un champ de saisie courriel
        txtCourriel = Entry(self, width=40)
        txtCourriel.grid(column=1, row=8)

        # Création d'un label numéro d'identification
        lblNumeroIdentification = Label(self, text="Numéro d'identification")
        lblNumeroIdentification.grid(column=0, row=9)

        # creation d'un champ de saisie numéro d'identification
        txtNumeroIdentification = Entry(self, width=40)
        txtNumeroIdentification.grid(column=1, row=9)

        # Création d'un label sexe
        lblSexe = Label(self, text="Sexe")
        lblSexe.grid(column=0, row=10)

        # creation d'un champ de saisie sexe
        txtSexe = Entry(self, width=40)
        txtSexe.grid(column=1, row=10)

        def ajouterClient():
            lstClients.insert(END, txtNom.get() + " " + txtPrenom.get())

        # Création d'un bouton ajouter
        btnAjouter = Button(self, text="Ajouter", command=ajouterClient)
        btnAjouter.grid(column=0, row=11)

        # petit espace
        lblEspace = Label(self, text="    ")
        lblEspace.grid(column=2, row=0)

        # création d'un label liste de clients
        lblListeClients = Label(self, text="Liste de clients")
        lblListeClients.grid(column=3, row=0)

        # création d'une liste de clients
        lstClients = Listbox(self, width=40)
        lstClients.grid(column=3, row=1)