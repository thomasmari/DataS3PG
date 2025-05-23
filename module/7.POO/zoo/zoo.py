from animal import Animal
from oiseau import Oiseau
from serpent import Serpent

class Zoo():
    def __init__(self,animal_list:list):
        self.__en_captivite=animal_list
    def liberer(self,a:Animal):
        if a in self.__en_captivite:
            self.__en_captivite.remove(a)
        else:
            raise ValueError("Cette Animal n'est pas en captivité")
    def capturer(self,a:Animal):
        self.__en_captivite.append(a)
    def pretty_print(self):
        for a in self.__en_captivite:
            a.pretty_print()

