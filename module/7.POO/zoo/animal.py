class Animal:
    def __init__(self,poids,taille):
        self.poids = poids
        self.taille = taille
    def se_deplacer(self):
        pass
        # return None
    def pretty_print(self):
        print(f"Animal qui pèse {self.poids} Kg et mesure {self.taille} m")

babar = Animal(358,2.3)
babar.se_deplacer()
babar.pretty_print()          