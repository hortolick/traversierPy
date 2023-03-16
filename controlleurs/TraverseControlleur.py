class TraverseController:
    def __init__(self, model, vue):
        self.model = model
        self.vue = vue

    def creerTraverse(self):
        self.model.noTraverse = self.vue.txtNoTraverse.get()
        self.model.dateHeure = self.vue.txtDateHeure.get()
        self.model.villeDepart = self.vue.txtVilleDepart.get()
        self.model.employeInscription = self.vue.txtEmployeInscription.get()
        print(self.model)