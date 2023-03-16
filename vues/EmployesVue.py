from tkinter import *

window = Tk()
window.title("Gestion des employés")
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

# Création d'un label adresse
lblAdresse = Label(window, text="Adresse")
lblAdresse.grid(column=0, row=2)

# creation d'un champ de saisie adresse
txtAdresse = Entry(window, width=40)
txtAdresse.grid(column=1, row=2)

# Création d'un label ville
lblVille = Label(window, text="Ville")
lblVille.grid(column=0, row=3)

# creation d'un champ de saisie ville
txtVille = Entry(window, width=40)
txtVille.grid(column=1, row=3)

# Création d'un label province
lblProvince = Label(window, text="Province")
lblProvince.grid(column=0, row=4)

# creation d'un champ de saisie province
txtProvince = Entry(window, width=40)
txtProvince.grid(column=1, row=4)

# Création d'un label code postal
lblCodePostal = Label(window, text="Code postal")
lblCodePostal.grid(column=0, row=5)

# creation d'un champ de saisie code postal
txtCodePostal = Entry(window, width=40)
txtCodePostal.grid(column=1, row=5)

# Création d'un label téléphone
lblTelephone = Label(window, text="Téléphone")
lblTelephone.grid(column=0, row=6)

# creation d'un champ de saisie téléphone
txtTelephone = Entry(window, width=40)
txtTelephone.grid(column=1, row=6)

# Création d'un label courriel
lblCourriel = Label(window, text="Courriel")
lblCourriel.grid(column=0, row=7)

# creation d'un champ de saisie courriel
txtCourriel = Entry(window, width=40)
txtCourriel.grid(column=1, row=7)

#creation d'un label numero d'emplye
lblNoEmploye = Label(window, text="Numéro d'employé")
lblNoEmploye.grid(column=0, row=8)

#creation d'un champ de saisie numero d'employe
txtNoEmploye = Entry(window, width=40)
txtNoEmploye.grid(column=1, row=8)

#creation d'un label numero d'assurance sociale
lblNAS = Label(window, text="Numéro d'assurance sociale")
lblNAS.grid(column=0, row=9)

#creation d'un champ de saisie numero d'assurance sociale
txtNAS = Entry(window, width=40)
txtNAS.grid(column=1, row=9)

#creation d'un label date d'embauche
lblDateEmbauche = Label(window, text="Date d'embauche")
lblDateEmbauche.grid(column=0, row=10)

#creation d'un champ de saisie date d'embauche
txtDateEmbauche = Entry(window, width=40)
txtDateEmbauche.grid(column=1, row=10)

#creation d'un label date d'arret
lblDateArret = Label(window, text="Date d'arret")
lblDateArret.grid(column=0, row=11)

#creation d'un champ de saisie date d'arret
txtDateArret = Entry(window, width=40)
txtDateArret.grid(column=1, row=11)

#creation d'un bouton ajouter
btnAjouter = Button(window, text="Ajouter")
btnAjouter.grid(column=0, row=12)

#creation d'une liste d'employes
lstEmployes = Listbox(window, width=40)
lstEmployes.grid(column=1, row=12)


window.mainloop()