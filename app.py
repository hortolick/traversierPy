from tkinter import *
from tkinter import ttk

import xml.etree.ElementTree as ET

from vues.TransStLaurent import TransStLaurentVue
from controlleurs.ClientControlleur import ClientControlleur
from modeles.Client import Client
from modeles.Employe import Employe
# from modeles.Personne import Personne
# from modeles.Vehicule import Vehicule
# from modeles.Traversier import Traversier
# from modeles.Traverse import Traverse

clients = []
employes = []
vehicules = []
traversiers = []
traverses = []

xmlroot = ET.parse("TransStLaurent.xml").getroot()

for clientxml in xmlroot.find("clients").findall("client"):
    client = Client(
        clientxml.get("nom"),
        clientxml.get("prenom"),
        clientxml.get("dateNaissance"),
        clientxml.get("adresse"),
        clientxml.get("ville"),
        clientxml.get("province"),
        clientxml.get("codePostal"),
        clientxml.get("telephone"),
        clientxml.get("courriel"),
        clientxml.get("numeroIdentification"),
        clientxml.get("sexe")
    )
    clients.append(client)


for employexml in xmlroot.find("employes").findall("employe"):
    employe = Employe(
        employexml.get("nom"),
        employexml.get("prenom"),
        employexml.get("dateNaissance"),
        employexml.get("adresse"),
        employexml.get("ville"),
        employexml.get("province"),
        employexml.get("codePostal"),
        employexml.get("telephone"),
        employexml.get("courriel"),
        employexml.get("noEmploye"),
        employexml.get("nAS"),
        employexml.get("dateEmbauche"),
        employexml.get("dateArret")
    )
    employes.append(employe)


for client in clients:
    print(client.__dict__)

window = Tk()
window.title("Transport St-Laurent")
window.geometry("640x480")

# Création d'un controleur de tab
tabControl = TransStLaurentVue(window)
tabControl.pack(expand=1, fill="both")
#client = Client()
clientControlleur = ClientControlleur(Client, tabControl.tabClients)
clientControlleur.remplirListeClients(clients)

window.mainloop()