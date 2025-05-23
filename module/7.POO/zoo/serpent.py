from animal import Animal

class Serpent(Animal):
    def __init__(self,poids,taille):
        super().__init__(poids,taille)
    def se_deplacer(self):
        print("tsssssssssss tsss     Je rampe      tsssssss  tssssssssss")
    def __str__(self):
        return(f"Serpent qui pèse {self.poids} Kg et mesure {self.taille} m")   