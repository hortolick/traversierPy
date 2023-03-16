import tkinter
from tkinter import *
from tkinter import ttk
from vues.EmployesVue import EmployesVue
from vues.ClientsVue import ClientsVue
from vues.TraversesVue import TraversesVue
from vues.TraversiersVue import TraversiersVue

class TransStLaurentVue(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Création d'un controleur de tab
        tabControl = ttk.Notebook(self)

        # Création et ajout d'un onglet Traverses
        tabTraverses = TraversesVue(tabControl)
        tabControl.add(tabTraverses, text='Traverses')

        # Création et ajout d'un onglet Traversiers
        tabTraversiers = TraversiersVue(tabControl)
        tabControl.add(tabTraversiers, text='Traversiers')

        # Création et ajout d'un onglet Employés
        tabEmployes = EmployesVue(tabControl)
        tabControl.add(tabEmployes, text='Employés')

        # Création et ajout d'un onglet Clients
        tabClients = ClientsVue(tabControl)
        tabControl.add(tabClients, text='Clients')

        # Création et ajout d'un onglet Véhicules
        #tabVehicules = ttk.Frame(tabControl)
        #tabControl.add(tabVehicules, text='Véhicules')


        tabControl.pack(expand=1, fill="both")
