from tkinter import *

class ClientsVue(Frame):
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

        #cretion d'un label Date de naissance
        self.lblDateNaissance = Label(self, text="Date de naissance")
        self.lblDateNaissance.grid(column=0, row=2)

        #creation d'un champ de saisie date de naissance
        self.txtDateNaissance = Entry(self, width=40)
        self.txtDateNaissance.grid(column=1, row=2)

        # Création d'un label adresse
        self.lblAdresse = Label(self, text="Adresse")
        self.lblAdresse.grid(column=0, row=3)

        # creation d'un champ de saisie adresse
        self.txtAdresse = Entry(self, width=40)
        self.txtAdresse.grid(column=1, row=3)

        # Création d'un label ville
        self.lblVille = Label(self, text="Ville")
        self.lblVille.grid(column=0, row=4)

        # creation d'un champ de saisie ville
        self.txtVille = Entry(self, width=40)
        self.txtVille.grid(column=1, row=4)

        # Création d'un label province
        self.lblProvince = Label(self, text="Province")
        self.lblProvince.grid(column=0, row=5)

        # creation d'un champ de saisie province
        self.txtProvince = Entry(self, width=40)
        self.txtProvince.grid(column=1, row=5)

        # Création d'un label code postal
        self.lblCodePostal = Label(self, text="Code postal")
        self.lblCodePostal.grid(column=0, row=6)

        # creation d'un champ de saisie code postal
        self.txtCodePostal = Entry(self, width=40)
        self.txtCodePostal.grid(column=1, row=6)

        # Création d'un label téléphone
        self.lblTelephone = Label(self, text="Téléphone")
        self.lblTelephone.grid(column=0, row=7)

        # creation d'un champ de saisie téléphone
        self.txtTelephone = Entry(self, width=40)
        self.txtTelephone.grid(column=1, row=7)

        # Création d'un label courriel
        self.lblCourriel = Label(self, text="Courriel")
        self.lblCourriel.grid(column=0, row=8)

        # creation d'un champ de saisie courriel
        self.txtCourriel = Entry(self, width=40)
        self.txtCourriel.grid(column=1, row=8)

        # Création d'un label numéro d'identification
        self.lblNumeroIdentification = Label(self, text="Numéro d'identification")
        self.lblNumeroIdentification.grid(column=0, row=9)

        # creation d'un champ de saisie numéro d'identification
        self.txtNumeroIdentification = Entry(self, width=40)
        self.txtNumeroIdentification.grid(column=1, row=9)

        # Création d'un label sexe
        self.lblSexe = Label(self, text="Sexe")
        self.lblSexe.grid(column=0, row=10)

        # creation d'un champ de saisie sexe
        self.txtSexe = Entry(self, width=40)
        self.txtSexe.grid(column=1, row=10)

        def ajouterClient():
            self.lstClients.insert(END, self.txtNom.get() + " " + self.txtPrenom.get())

        # Création d'un bouton ajouter
        self.btnAjouter = Button(self, text="Ajouter", )
        self.btnAjouter.grid(column=0, row=11)

        # petit espace
        self.lblEspace = Label(self, text="    ")
        self.lblEspace.grid(column=2, row=0)

        # création d'un label liste de clients
        self.lblListeClients = Label(self, text="Liste de clients")
        self.lblListeClients.grid(column=3, row=0)

        # création d'une liste de clients
        self.lstClients = Listbox(self, width=40)
        self.lstClients.grid(column=3, row=1)