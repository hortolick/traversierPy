from modeles.Personne import Personne
import datetime

class Employe(Personne):
    def __init__(self, nom="", prenom = "", dateNaissance = datetime.datetime.now(), adresse="", ville="", province="", codePostal="", telephone="", courriel="", noEmploye="", nAS="", dateEmbauche=datetime.datetime.now(), dateArret=datetime.datetime.now()):
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance
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