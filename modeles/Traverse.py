import datetime
import Employe
import Client
import Vehicule

class Traverse:
    def __init__(self, noTraverse = 0, dateHeure = datetime.datetime.now(), villeDepart = "", employeInscription = Employe.Employe(), listeVehicule = [], listeClient = []):
        self.noTraverse = noTraverse
        self.dateHeure = dateHeure
        self.villeDepart = villeDepart
        self.employeInscription = employeInscription
        self.listeVehicule = listeVehicule
        self.listeClient = listeClient

        def obtenirListeVehicule(self):
            return self.listeVehicule

        def obtenirUnVehicule(self, noVehicule:int):
            for vehicule in self.listeVehicule:
                if vehicule.noVehicule == noVehicule:
                    return vehicule

        def ajouterVehicule(self, vehicule:Vehicule):
            self.listeVehicule.append(vehicule)

        def modifierVehicule(self, vehiculeModifie:Vehicule):
            for vehicule in self.listeVehicule:
                if vehicule.noVehicule == vehicule.noVehicule:
                    vehicule = vehiculeModifie

        def supprimerVehicule(self, noVehicule:int):
            for vehicule in self.listeVehicule:
                if vehicule.noVehicule == noVehicule:
                    self.listeVehicule.remove(vehicule)

        def obtenirListeClient(self):
            return self.listeClient

        def obtenirUnClient(self, noClient:int):
            for client in self.listeClient:
                if client.noClient == noClient:
                    return client

        def ajouterClient(self, client:Client):
            self.listeClient.append(client)

        def modifierClient(self, clientModifie:Client):
            for client in self.listeClient:
                if client.noClient == client.noClient:
                    client = clientModifie

        def supprimerClient(self, noClient:int):
            for client in self.listeClient:
                if client.noClient == noClient:
                    self.listeClient.remove(client)