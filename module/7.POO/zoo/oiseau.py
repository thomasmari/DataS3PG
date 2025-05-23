from animal import Animal

class Oiseau(Animal):
    def __init__(self,poids,taille):
        super().__init__(poids,taille)
    def se_deplacer(self):
        print("flap flap flap             Je Vole !       flap flap flap")

