from tkinter import *
from tkinter import ttk

from vues.TransStLaurent import TransStLaurentVue
from controlleurs.ClientControlleur import ClientControlleur
from modeles.Client import Client
from vues.ClientsVue import ClientsVue

window = Tk()
window.title("Transport St-Laurent")
window.geometry("640x480")

# Création d'un controleur de tab
tabControl = TransStLaurentVue(window)
tabControl.pack(expand=1, fill="both")
print ("uooiuo")
client = Client()
clientControlleur = ClientControlleur(client, tabControl.tabClients)

window.mainloop()