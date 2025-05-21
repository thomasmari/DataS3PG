from statistics import median
# ----------------
# Fonctions d'aide
# ----------------
def swap(tab, i, j): # side-effect on tab
    """Échange la place des éléments aux indices i et j du tableau"""
    tmp = tab[i]
    tab[i] = tab[j]
    tab[j] = tmp
    return None


# ---------------
# Tris classiques
# ---------------
def bubble_sort(tab):
    """Trie le tableau en déplaçant les plus grosses valeurs vers la fin du
    tableau, un peu comme des bulles dans l'eau qui remonteraient à la
    surface"""
    B = tab.copy()
    for i in range(len(B)-1,0,-1):
        for j in range(0,i):
            if B[j+1] < B[j]:
                swap(B,j,j+1)
    return B


def insertion_sort(tab):
    """Trie le tableau en plaçant l'élément courant à la bonne place dans
    le sous-tableau déjà trié"""
    tab_s = []
    for e in tab:
        added=False
        for i in range(len(tab_s)):
            if e < tab_s[i]:
                tab_s.insert(i, e)
                added = True
                break
        if not added:
            tab_s.append(e)
    return tab_s



def selection_sort(tab):
    """Trie le tableau en cherchant le plus petit élément à mettre dans la
    première case, puis le second plus petit à mettre dans la seconde case,
    etc"""
    n = len(tab)
    B=tab.copy()
    for i in range(0,n-2):
        mini = i
        for j in range(i+1,n):
            if B[j] < B[mini]:
                mini = j
        if mini != i:
            swap(B,i,mini)
    return B

# --------------
# Tris récursifs
# --------------
def merge_list(tab1,tab2):
    """merge and return the sorted union of two sorted List """
    i1,i2=0,0
    n1,n2=len(tab1),len(tab2)
    tab12 = []
    while not (i1==n1 and i2==n2):
        if i1 == n1:
            return tab12+tab2[i2:n2]
        elif i2 == n2:
            return tab12+tab1[i1:n1]
        elif tab1[i1]<tab2[i2]:
            tab12.append(tab1[i1])
            i1+=1
        else:
            tab12.append(tab2[i2])
            i2+=1
    return tab12


def merge_sort(tab):
    """Trie le tableau via le principe de « diviser pour mieux régner »
    avec l'intelligence du tri qui se trouve au moment de la fusion"""
    n=len(tab)
    if n <=1:
        return tab
    else:
        mid = len(tab)//2
        tab1=merge_sort(tab[0:mid])
        tab2=merge_sort(tab[mid:n])
        tab12=merge_list(tab1,tab2) 
        return tab12

def pivot(tab):
    """return ltab,pivot,rtab """
    p = tab[0]
    ltab = [e for e in tab[1:] if e < p]
    rtab = [e for e in tab[1:] if e >= p]
    return ltab,p,rtab

def quick_sort(tab):
    """Divise le tableau en deux, trie chacune des sous-parties et fusionne
    intelligemment les deux sous-parties triées"""
    n=len(tab)
    if n<=1:
        return tab
    ltab,p,rtab = pivot(tab)
    return quick_sort(ltab) + [p] + quick_sort(rtab)

def smart_pivot(tab):
    """return ltab,pivot,rtab ou le pivot est l'elmt le plus proche de la mediane"""
    # trouver le pivot telle que pivot ~= mediane
    med = median(tab)
    n = len(tab)
    imed = 0
    for i in range(1,n):
        if abs(tab[i]-med) < abs(tab[imed]-med):
            imed = i
    #return the partition
    p=tab[imed]
    ltab = [e for e in tab[0:imed]+tab[imed+1:] if e < p]
    rtab = [e for e in tab[0:imed]+tab[imed+1:] if e >= p]
    return ltab,p,rtab

def quick_smart_sort(tab):
    """Divise le tableau en deux, trie chacune des sous-parties et fusionne
    intelligemment les deux sous-parties triées"""
    n=len(tab)
    if n<=1:
        return tab
    ltab,p,rtab = smart_pivot(tab)
    return quick_smart_sort(ltab) + [p] + quick_smart_sort(rtab)