from modeles.Personne import Personne
import datetime

class Client(Personne):
    def __init__(self, nom="", prenom = "", dateNaissance = datetime.datetime.now(), adresse="", ville="", province="", codePostal="", telephone="", courriel="", numeroIdentification="", sexe=""):
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance
        self.adresse = adresse
        self.ville = ville
        self.province = province
        self.codePostal = codePostal
        self.telephone = telephone
        self.courriel = courriel
        self.numeroIdentification = numeroIdentification
        self.sexe = sexe