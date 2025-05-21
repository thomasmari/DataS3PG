import random
from sorting import insertion_sort


def create_deck():
   deck = list()
   couleurs = ["carreau", "coeur", "pique", "trefle", "joker"]
   for couleur in couleurs:
       if couleur=="joker":
           hauteurs = [i for i in range(1,3)]
       else:
           hauteurs = [i for i in range(1,14)]
       for hauteur in hauteurs:
           deck.append((couleur, hauteur))
   random.shuffle(deck)
   return(deck)

def partition_deck(deck_cards):
    partition = {"carreau":[], "coeur":[], "pique":[], "trefle":[], "joker":[]}
    for (color,height) in deck_cards:
        (partition[color]).append((color,height))    
    return(partition)


def tri_cartes():
    return None
  
if __name__ == "__main__":
    couleurs = ["carreau", "coeur", "pique", "trefle", "joker"]
    deck = create_deck()
    print(f"Unsorted deck:\n{deck}")
    print(f"1 ère partie: tri par couleur + joker")
    part = partition_deck(deck)
    # print(part)
    print(f"2ème partie: tri de chaque pile par hauteur, sauf la pile du joker")
    sort_pile = []
    for color in ["carreau", "coeur", "pique", "trefle"]:
        l = insertion_sort([i for (c,i) in part[color]])
        sort_pile += [(color,i) for i in l]
    print(f"3ème partie: pile finale")
    sort_pile+=part["joker"]
    print(sort_pile)

