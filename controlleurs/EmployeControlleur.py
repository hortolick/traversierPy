class EmployeControlleur:
    def __init__(self, model, vue):
        self.model = model
        self.vue = vue
        self.vue.btnAjouter.config(command=lambda: self.creerEmploye())

    def creerEmploye(self):
        self.model.nom = self.vue.txtNom.get()
        self.model.prenom = self.vue.txtPrenom.get()
        self.model.adresse = self.vue.txtAdresse.get()
        self.model.ville = self.vue.txtVille.get()
        self.model.province = self.vue.txtProvince.get()
        self.model.codePostal = self.vue.txtCodePostal.get()
        self.model.telephone = self.vue.txtTelephone.get()
        self.model.courriel = self.vue.txtCourriel.get()
        self.model.noEmploye = self.vue.txtNoEmploye.get()
        self.model.nAS = self.vue.txtNAS.get()
        self.model.dateEmbauche = self.vue.txtDateEmbauche.get()
        self.model.dateArret = self.vue.txtDateArret.get()
        print(self.model.nom, self.model.prenom, self.model.adresse, self.model.ville, self.model.province, self.model.codePostal, self.model.telephone, self.model.courriel, self.model.noEmploye, self.model.dateEmbauche, self.model.dateArret, self.model.nAS)