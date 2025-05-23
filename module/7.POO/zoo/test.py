from animal import Animal 
from oiseau import Oiseau 
from serpent import Serpent 
from zoo import Zoo

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
    print("Poulet mange des graines et prends du poids")  
    poulet.set_poids(poulet.get_poids()+0.1)
    poulet.pretty_print() 
    print("Création d'un nouveau Zoo")
    zoo_de_grenoble = Zoo([babar])
    zoo_de_grenoble.capturer(vipere)
    zoo_de_grenoble.capturer(poulet)
    zoo_de_grenoble.pretty_print()
    print("Les Animaux s'échappe à travers la porte mais babar ne passe pas")
    zoo_de_grenoble.liberer(vipere)
    zoo_de_grenoble.liberer(poulet)
    zoo_de_grenoble.pretty_print()



