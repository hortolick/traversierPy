from tkinter import *

window = Tk()
window.title("Gestion des Clients")
window.geometry("640x480")

# Création d'un label Nom
lblNom = Label(window, text="Nom")
lblNom.grid(column=0, row=0)

# creation d'un champ de saisie nom
txtNom = Entry(window, width=40)
txtNom.grid(column=1, row=0)

# Création d'un label Prénom
lblPrenom = Label(window, text="Prénom")
lblPrenom.grid(column=0, row=1)

# creation d'un champ de saisie prénom
txtPrenom = Entry(window, width=40)
txtPrenom.grid(column=1, row=1)

#cretion d'un label Date de naissance
lblDateNaissance = Label(window, text="Date de naissance")
lblDateNaissance.grid(column=0, row=2)

#creation d'un champ de saisie date de naissance
txtDateNaissance = Entry(window, width=40)
txtDateNaissance.grid(column=1, row=2)

# Création d'un label adresse
lblAdresse = Label(window, text="Adresse")
lblAdresse.grid(column=0, row=3)

# creation d'un champ de saisie adresse
txtAdresse = Entry(window, width=40)
txtAdresse.grid(column=1, row=3)

# Création d'un label ville
lblVille = Label(window, text="Ville")
lblVille.grid(column=0, row=4)

# creation d'un champ de saisie ville
txtVille = Entry(window, width=40)
txtVille.grid(column=1, row=4)

# Création d'un label province
lblProvince = Label(window, text="Province")
lblProvince.grid(column=0, row=5)

# creation d'un champ de saisie province
txtProvince = Entry(window, width=40)
txtProvince.grid(column=1, row=5)

# Création d'un label code postal
lblCodePostal = Label(window, text="Code postal")
lblCodePostal.grid(column=0, row=6)

# creation d'un champ de saisie code postal
txtCodePostal = Entry(window, width=40)
txtCodePostal.grid(column=1, row=6)

# Création d'un label téléphone
lblTelephone = Label(window, text="Téléphone")
lblTelephone.grid(column=0, row=7)

# creation d'un champ de saisie téléphone
txtTelephone = Entry(window, width=40)
txtTelephone.grid(column=1, row=7)

# Création d'un label courriel
lblCourriel = Label(window, text="Courriel")
lblCourriel.grid(column=0, row=8)

# creation d'un champ de saisie courriel
txtCourriel = Entry(window, width=40)
txtCourriel.grid(column=1, row=8)

# Création d'un label numéro d'identification
lblNumeroIdentification = Label(window, text="Numéro d'identification")
lblNumeroIdentification.grid(column=0, row=9)

# creation d'un champ de saisie numéro d'identification
txtNumeroIdentification = Entry(window, width=40)
txtNumeroIdentification.grid(column=1, row=9)

# Création d'un label sexe
lblSexe = Label(window, text="Sexe")
lblSexe.grid(column=0, row=10)

# creation d'un champ de saisie sexe
txtSexe = Entry(window, width=40)
txtSexe.grid(column=1, row=10)

# Création d'un bouton ajouter
btnAjouter = Button(window, text="Ajouter")
btnAjouter.grid(column=0, row=11)

# création d'une liste de clients
lstClients = Listbox(window, width=40)
lstClients.grid(column=1, row=11)



window.mainloop()