from tkinter import *

window = Tk()
window.title("Gestion des traversiers")
window.geometry("640x480")

# Création d'un label Nom
lblNom = Label(window, text="Nom")
lblNom.grid(column=0, row=0)

# creation d'un champ de saisie nom
txtNom = Entry(window, width=40)
txtNom.grid(column=1, row=0)

# Création d'un label capacité vehicule
lblCapaciteVehicule = Label(window, text="Capacité véhicule")
lblCapaciteVehicule.grid(column=0, row=1)

# creation d'un champ de saisie capacité vehicule
txtCapaciteVehicule = Entry(window, width=40)
txtCapaciteVehicule.grid(column=1, row=1)

# Création d'un label capacité personne
lblCapacitePersonne = Label(window, text="Capacité personne")
lblCapacitePersonne.grid(column=0, row=2)

# creation d'un champ de saisie capacité personne
txtCapacitePersonne = Entry(window, width=40)
txtCapacitePersonne.grid(column=1, row=2)

# Création d'un label annee fabrication
lblAnneeFabrication = Label(window, text="Année fabrication")
lblAnneeFabrication.grid(column=0, row=3)

# creation d'un champ de saisie annee fabrication
txtAnneeFabrication = Entry(window, width=40)
txtAnneeFabrication.grid(column=1, row=3)

# Création d'un label date de mise en service
lblDateMiseEnService = Label(window, text="Date de mise en service")
lblDateMiseEnService.grid(column=0, row=4)

# creation d'un champ de saisie date de mise en service
txtDateMiseEnService = Entry(window, width=40)
txtDateMiseEnService.grid(column=1, row=4)

# Création d'un label liste employes
lblListeEmployes = Label(window, text="Liste employés")
lblListeEmployes.grid(column=0, row=5)

# creation d'une liste employes
txtListeEmployes = Entry(window, width=40)
txtListeEmployes.grid(column=1, row=5)

# Création d'un bouton ajouter
btnAjouter = Button(window, text="Ajouter")
btnAjouter.grid(column=0, row=6)

window.mainloop()
