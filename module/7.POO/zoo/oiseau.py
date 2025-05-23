from animal import Animal

class Oiseau(Animal):
    def __init__(self,poids,taille,altitude=0):
        super().__init__(poids,taille)
        self.altitude_max = altitude
    def se_deplacer(self):
        print(f"flap flap flap             Je Vole ! Je peux voler J'usquà {self.altitude_max}  m    flap flap flap")
    def __str__(self):
        return(f"oiseau  qui pèse {self.poids} Kg et mesure {self.taille} m")   
