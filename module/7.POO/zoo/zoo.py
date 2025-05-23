from animal import Animal
from oiseau import Oiseau
from serpent import Serpent

class Zoo():
    def __init__(self,animal_list:list):
        self.__en_captivite=animal_list
    def get_animal_list(self):
        return(self.__en_captivite.copy())
    def __add__(self,zoobis):
        return(Zoo(self.get_animal_list() + zoobis.get_animal_list()))
    def liberer(self,a:Animal):
        if a in self.__en_captivite:
            self.__en_captivite.remove(a)
        else:
            raise ValueError("Cette Animal n'est pas en captivité")
    def capturer(self,a:Animal):
        self.__en_captivite.append(a)
    def __str__(self):
        str_list = ["Voici les animaux du zoo:"]
        for a in self.__en_captivite:
            str_list.append(a.__str__())
        return("\n\t".join(str_list))
    def pretty_print(self):
        print(self.__str__())


