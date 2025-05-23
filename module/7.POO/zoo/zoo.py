from animal import Animal
from oiseau import Oiseau
from serpent import Serpent

class Zoo():
    def __init__(self,animal_list:list):
        self.en_captivite=animal_list
    @property
    def en_captivite(self):
        return(self.__en_captivite)
    @en_captivite.setter
    def en_captivite(self,animal_list:list):
        for a in animal_list:
            if not(isinstance(a,Animal)):
                raise ValueError("Only animals of class Animal can be added to a Zoo")
        self.__en_captivite = animal_list
    def __add__(self,zoobis):
        return(Zoo(self.en_captivite + zoobis.en_captivite))
    def liberer(self,a:Animal):
        if a in self.__en_captivite:
            self.en_captivite.remove(a)
        else:
            raise ValueError("Cette Animal n'est pas en captivité")
    def capturer(self,a:Animal):
        if not(isinstance(a,Animal)):
            raise ValueError("Only animals of class Animal can be added to a Zoo")
        self.en_captivite.append(a)
    def __str__(self):
        str_list = ["Voici les animaux du zoo:"]
        for a in self.__en_captivite:
            str_list.append(a.__str__())
        return("\n\t".join(str_list))
    def pretty_print(self):
        print(self.__str__())


