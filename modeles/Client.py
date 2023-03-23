from modeles.Personne import Personne
import datetime

class Client(Personne):
    def __init__(self, nom="", adresse="", ville="", province="", codePostal="", telephone="", courriel="", numeroIdentification="", sexe="", dateNaissance=datetime.datetime.now()):
        self.nom = nom
        self.adresse = adresse
        self.ville = ville
        self.province = province
        self.codePostal = codePostal
        self.telephone = telephone
        self.courriel = courriel
        self.numeroIdentification = numeroIdentification
        self.sexe = sexe
        self.dateNaissance = dateNaissance