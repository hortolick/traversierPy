import datetime
import Employe
import Client
import Vehicule

class Traverse:
    def __init__(self, noTraverse:int, dateHeure:datetime, villeDepart:str, employeInscription:Employe, listeVehicule:list, listeClient:list):
        self.noTraverse = noTraverse
        self.dateHeure = dateHeure
        self.villeDepart = villeDepart
        self.employeInscription = employeInscription
        self.listeVehicule = listeVehicule
        self.listeClient = listeClient
