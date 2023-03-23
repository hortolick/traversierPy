from modeles.Personne import Personne
import datetime

class Employe(Personne):
    def __init__(self, nom: str, adresse: str, ville: str, province: str, codePostal: str, telephone: str, courriel: str, noEmploye:int, nAS:int, dateEmbauche:datetime, dateArret:datetime):
        self.nom = nom
        self.adresse = adresse
        self.ville = ville
        self.province = province
        self.codePostal = codePostal
        self.telephone = telephone
        self.courriel = courriel
        self.noEmploye = noEmploye
        self.nAS = nAS
        self.dateEmbauche = dateEmbauche
        self.dateArret = dateArret