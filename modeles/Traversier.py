import datetime
import Employe

class Traversier:
    def __init__(self, nom:str, capaciteVehicule:int, capacitePersonne:int, anneeFabrication:datetime, dateMiseService:datetime, listeEmploye:list):
        self.nom = nom
        self.capaciteVehicule = capaciteVehicule
        self.capacitePersonne = capacitePersonne
        self.anneeFabrication = anneeFabrication
        self.dateMiseService = dateMiseService
        self.listeEmploye = listeEmploye