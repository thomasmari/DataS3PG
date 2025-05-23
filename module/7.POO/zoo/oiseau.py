from animal import Animal

class Oiseau(Animal):
    def __init__(self,poids,taille,altitude=0):
        super().__init__(poids,taille)
        self.altitude_max = altitude
    def se_deplacer(self):
        print(f"flap flap flap             Je Vole ! Je peux voler J'usquà {self.altitude_max}  m    flap flap flap")
    def pretty_print(self):
        print(f"oiseau  qui pèse {self.get_poids()} Kg et mesure {self.get_taille()} m")   
