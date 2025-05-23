from animal import Animal

class Serpent(Animal):
    def __init__(self,poids,taille):
        super().__init__(poids,taille)
    def se_deplacer(self):
        print("tsssssssssss tsss     Je rampe      tsssssss  tssssssssss")
    def pretty_print(self):
        print(f"Serpent qui pèse {self.get_poids()} Kg et mesure {self.get_taille()} m")   