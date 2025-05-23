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
    poulet.poids = poulet.poids+0.1
    poulet.pretty_print() 
    print("babar dort la nuit et grandit de 2cm")  
    babar.taille =  babar.taille+0.02
    babar.pretty_print()
    print("Création d'un nouveau Zoo")
    zoo_de_grenoble = Zoo([babar])
    zoo_de_grenoble.capturer(vipere)
    zoo_de_grenoble.capturer(poulet)
    zoo_de_grenoble.pretty_print()
    print("Les Animaux s'échappe à travers la porte mais babar ne passe pas")
    zoo_de_grenoble.liberer(vipere)
    zoo_de_grenoble.liberer(poulet)
    zoo_de_grenoble.pretty_print()
    print("Création d'un nouveau zoo de la voliere de Mélan")
    pigeon1 =  Oiseau(0.150,0.23,altitude = 10)
    pigeon2 =  Oiseau(0.160,0.25,altitude = 10**5)
    pigeon3 =  Oiseau(0.130,0.27,altitude = 100/3)
    zoo_de_melan = Zoo([pigeon1,pigeon2,pigeon3])   
    print("zoo de grenoble + zoo de melan")
    (zoo_de_grenoble+zoo_de_melan).pretty_print()






