class Animal:
    def __init__(self,poids_kg:float,taille_m:float):
        self.poids = poids_kg
        self.taille = taille_m
    ## setter and getter
    # def get_poids(self):
    #     return(self.__poids)
    # def set_poids(self,nouveau_poids:float):
    #     if nouveau_poids > 0:
    #         self.__poids = nouveau_poids
    #     else:
    #         raise ValueError("L'argument nouveau_poids doit être un float strictement positif")    
    # def get_taille(self):
    #     return(self.__taille)
    # def set_taille(self,nouvelle_taille:float):
    #     if nouvelle_taille > 0:
    #         self.__taille = nouvelle_taille
    #     else:
    #         raise ValueError("L'argument nouvelle_taille doit être un float strictement positif")
    @property
    def poids(self):
        return(self.__poids)
    @poids.setter
    def poids(self,nouveau_poids:float):
        if nouveau_poids > 0:
            self.__poids = nouveau_poids
        else:
            raise ValueError("L'argument nouveau_poids doit être un float strictement positif")    
    @property
    def taille(self):
        return(self.__taille)
    @taille.setter
    def taille(self,nouvelle_taille:float):
        if nouvelle_taille > 0:
            self.__taille = nouvelle_taille
        else:
            raise ValueError("L'argument nouvelle_taille doit être un float strictement positif")
    # ## Property
    # @property
    # def poids(self):
    #     return(self.get_poids())
    # @property
    # def taille(self):
    #     return(self.get_taille())    
    # ## the attribute name and the method name must be same which is used to set the value for the attribute
    # @poids.setter
    # def poids(self, var):
    #     self.set_poids(var)
    # @taille.setter
    # def taille(self, var):
    #     self.set_taille(var)
    # Methods
    def se_deplacer(self):
        pass #remember to implement this
    def __str__(self):
        return(f"Animal qui pèse {self.poids} Kg et mesure {self.taille} m")   
    def pretty_print(self):
        print(self.__str__())       