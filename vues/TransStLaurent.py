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
        self.tabControl = ttk.Notebook(self)

        # Création et ajout d'un onglet Traverses
        self.tabTraverses = TraversesVue(self.tabControl)
        self.tabControl.add(self.tabTraverses, text='Traverses')

        # Création et ajout d'un onglet Traversiers
        self.tabTraversiers = TraversiersVue(self.tabControl)
        self.tabControl.add(self.tabTraversiers, text='Traversiers')

        # Création et ajout d'un onglet Employés
        self.tabEmployes = EmployesVue(self.tabControl)
        self.tabControl.add(self.tabEmployes, text='Employés')

        # Création et ajout d'un onglet Clients
        self.tabClients = ClientsVue(self.tabControl)
        self.tabControl.add(self.tabClients, text='Clients')

        # Création et ajout d'un onglet Véhicules
        self.tabVehicules = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabVehicules, text='Véhicules')


        self.tabControl.pack(expand=1, fill="both")
