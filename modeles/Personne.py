import datetime


class Personne:
    def __init__(self, nom = "", prenom = "", dateNaissance = datetime.datetime.now(), adresse = "", ville = "", province = "", codePostal = "", telephone = "", courriel = ""):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.ville = ville
        self.province = province
        self.codePostal = codePostal
        self.telephone = telephone
        self.courriel = courriel