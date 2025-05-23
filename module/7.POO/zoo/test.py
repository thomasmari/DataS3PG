from animal import Animal 
from oiseau import Oiseau 
from serpent import Serpent 

if __name__ == '__main__':
    babar = Animal(358,2.3)
    babar.se_deplacer()
    babar.pretty_print()   
    vipere = Serpent(0.58,1.2)
    vipere.se_deplacer()
    vipere.pretty_print()   
    poulet = Oiseau(0.300,0.23)
    poulet.se_deplacer()
    poulet.pretty_print()   

