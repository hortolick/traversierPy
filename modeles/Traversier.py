import datetime
import Employe

class Traversier:
    def __init__(self, nom = "", capaciteVehicule=0, capacitePersonne=0, anneeFabrication=datetime.datetime.year, dateMiseService=datetime.datetime.now(), listeEmploye=[] ):
        self.nom = nom
        self.capaciteVehicule = capaciteVehicule
        self.capacitePersonne = capacitePersonne
        self.anneeFabrication = anneeFabrication
        self.dateMiseService = dateMiseService
        self.listeEmploye = listeEmploye