import tkinter
from tkinter import *
from tkinter import ttk
from EmployesVue import VueEmployes
from ClientsVue import VueClients
from TraversesVue import VueTraverses
from TraversiersVue import VueTraversiers

window = Tk()
window.title("Transport St-Laurent")
window.geometry("640x480")

# Création d'un controleur de tab
tabControl = ttk.Notebook(window)

# Création et ajout d'un onglet Traverses
tabTraverses = VueTraverses(tabControl)
tabControl.add(tabTraverses, text='Traverses')

# Création et ajout d'un onglet Traversiers
tabTraversiers = VueTraversiers(tabControl)
tabControl.add(tabTraversiers, text='Traversiers')

# Création et ajout d'un onglet Employés
tabEmployes = VueEmployes(tabControl)
tabControl.add(tabEmployes, text='Employés')

# Création et ajout d'un onglet Clients
tabClients = VueClients(tabControl)
tabControl.add(tabClients, text='Clients')

# Création et ajout d'un onglet Véhicules
#tabVehicules = ttk.Frame(tabControl)
#tabControl.add(tabVehicules, text='Véhicules')


tabControl.pack(expand=1, fill="both")
window.mainloop()
