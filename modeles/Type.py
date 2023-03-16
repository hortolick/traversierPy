import decimal
class Type:
    def __init__(self, nom:str, nombreRoute:bytes, prixTraverse:decimal):
        self.nom = nom
        self.nombreRoute = nombreRoute
        self.prixTraverse = prixTraverse