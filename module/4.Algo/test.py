import random
from sorting import *

def generate_random_array(debug=False, N=21):
    """Renvoie un tableau contenant toutes les valeurs entières de 0 (inclus)
    à N (exclus) rangées dans un ordre aléatoire

    Args:
        debug (boolean): quand debug est vrai, la fonction renvoie toujours le
                         même tableau afin de simplifier le débogage de vos
                         algorithmes de tri
        N (int): la taille du tableau à renvoyer

    Returns:
        list[int]: un tableau d'entiers, de taille N, non ordonné
    """

    if debug:
        return [3, 9, 7, 1, 6, 2, 8, 4, 5, 0]

    array = list(range(0, N))
    random.shuffle(array)

    return array


def test(sort_function,A=None):
    if A == None:
        A = (generate_random_array(N=100))
    return sort_function(A)

# print(test(insertion_sort))
# print(test(selection_sort))
# print(test(bubble_sort))
# print(test(merge_sort))
# print(test(quick_sort))
# print(test(quick_smart_sort))


    
