import decimal
class Type:
    def __init__(self, nom = "", nombreRoute = 0, prixTraverse = decimal.Decimal(0.00)):
        self.nom = nom
        self.nombreRoute = nombreRoute
        self.prixTraverse = prixTraverse