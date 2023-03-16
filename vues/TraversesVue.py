from tkinter import *

window = Tk()
window.title("Gestion des Traverses")
window.geometry("640x480")

# Création d'un label numero traverse
lblNoTraverse = Label(window, text="Numéro de traverse")
lblNoTraverse.grid(column=0, row=0)

# creation d'un champ de saisie numero traverse
txtNoTraverse = Entry(window, width=40)
txtNoTraverse.grid(column=1, row=0)

# Création d'un label date hure
lblDateHeure = Label(window, text="Date et heure")
lblDateHeure.grid(column=0, row=1)

# creation d'un champ de saisie date heure
txtDateHeure = Entry(window, width=40)
txtDateHeure.grid(column=1, row=1)

# Création d'un label employe inscription
lblEmployeInscription = Label(window, text="Employé inscription")
lblEmployeInscription.grid(column=0, row=2)

# creation d'une liste déroulante employe inscription
txtEmployeInscription = Entry(window, width=40)
txtEmployeInscription.grid(column=1, row=2)

# Création d'une liste vehicule
lstVehicule = Listbox(window, width=40)
lstVehicule.grid(column=1, row=3)

# création d'une liste client
lstClient = Listbox(window, width=40)
lstClient.grid(column=1, row=4)

# Création d'un bouton ajouter
btnAjouter = Button(window, text="Ajouter")
btnAjouter.grid(column=0, row=4)

window.mainloop()