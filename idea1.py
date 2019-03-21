import copy as cp
import random as rnd
import time

taille = 3


# done une liste de taille ellements [0;taille*taille[
def newlist(taille):
    temp = list()
    for i in range(taille * taille):
        temp.append(i)
    return temp

# transforme une liste dans un taquin
def newTaquin(l, taille):
    taquin = list()
    spot = taille - 1
    ml = list()
    for i in range(0, taille * taille):
        ml.append(l[i])
        if (i == spot):
            taquin.append(ml.copy())
            ml.clear()
            spot = spot + taille
    return taquin

# imprime le taquin
def printTaquin(taquin):
    for i in range(len(taquin)):
        print(taquin[i])
    print()

# retourne 0 si la piecen'est pas dans le taquin
def find(taquin, element):
    # si an element existe dans le taquin renvoi ca position sinon renvoi 0
    if element >= (len(taquin) * len(taquin)):
        return 0
    else:
        foundit = False
        position = [0]
        while foundit == False:
            for y in range(0, len(taquin[0])):
                for x in range(0, len(taquin[0])):
                    if taquin[y][x] == element:
                        position = [x, y]
                        foundit = True
        return position

# fonction qui retouve vrai si deuz taquins egals
def compare(taquin1, taquin2):
    result = True
    if len(taquin1) != len(taquin2):
        result = False
    else:
        for y in range(len(taquin1)):
            for x in range(len(taquin1)):
                if taquin1[y][x] != taquin2[y][x]:
                    result = False
        return result

# =============bouger la casa vide======================
# retuns vrai si un mouvement est possible faux si non
def possible(taquin, move):
    caseVide = (len(taquin) * len(taquin) - 1)
    position = find(taquin, caseVide)  # porition=[x,y]
    x = position[0]
    y = position[1]
    reponse = False
    if move == "H" or move == "h":  # case videen haut
        if y >= 1 and y <= (len(taquin) - 1):
            reponse = True
    elif move == "B" or move == "b":  # case vide en bas
        if y >= 0 and y <= (len(taquin) - 2):
            reponse = True
    elif move == "D" or move == "d":  # case vide a droite
        if x >= 0 and x <= (len(taquin) - 2):
            reponse = True
    elif move == "G" or move == "g":  # case videa gauche
        if x >= 1 and x <= (len(taquin) - 1):
            reponse = True
    return reponse

# bouge la piece vide en hau
def mH(taquin):
    temp = cp.deepcopy(taquin)
    position = find(taquin, (len(taquin) * len(taquin) - 1))
    x = position[0]
    y = position[1]
    temp[y][x] = taquin[y - 1][x]  # la case d'en haut est copier en bas
    temp[y - 1][x] = taquin[y][x]
    return temp

# bouge la piece vide en bas
def mB(taquin):
    temp = cp.deepcopy(taquin)
    position = find(taquin, (len(taquin) * len(taquin) - 1))
    x = position[0]
    y = position[1]
    temp[y][x] = taquin[y + 1][x]  # la case d'en bas est copier en haut
    temp[y + 1][x] = taquin[y][x]  # position de la case vide
    return temp

# bouge la piece vide a droite
def mD(taquin):
    temp = cp.deepcopy(taquin)
    position = find(taquin, (len(taquin) * len(taquin) - 1))
    x = position[0]
    y = position[1]
    temp[y][x] = taquin[y][x + 1]
    temp[y][x + 1] = taquin[y][x]  # position de la case vide
    return temp

# bouge la pece vide a gauche
def mG(taquin):
    temp = cp.deepcopy(taquin)
    position = find(taquin, (len(taquin) * len(taquin) - 1))
    x = position[0]
    y = position[1]
    temp[y][x] = taquin[y][x - 1]
    temp[y][x - 1] = taquin[y][x]
    return temp

# efevtue les 4 mouvements possibles sur demande
def bouger(taquin, direction):
    tac = cp.deepcopy(taquin)
    if direction == "H" or direction == "h":  # case videen haut
        tac = mH(taquin)
    elif direction == "B" or direction == "b":  # case vide en bas
        tac = mB(taquin)
    elif direction == "D" or direction == "d":  # case vide a droite
        tac = mD(taquin)
    elif direction == "G" or direction == "g":  # case videa gauche
        tac = mG(taquin)
    return tac

# fonction qui melange un taquin
def melanger(taquin, numero):
    if numero == 0:
        return taquin
    else:
        for ct in range(numero):
            mvm = rnd.choice("HDBG")
            if possible(taquin, mvm) is False:
                while possible(taquin, mvm) is False:
                    mvm = rnd.choice("HDBG")
            if mvm == "H":
                taquin=mH(taquin)
            if mvm == "B":
                taquin=mB(taquin)
            if mvm == "D":
                taquin=mD(taquin)
            if mvm == "G":
                taquin=mG(taquin)
    return taquin
# ========================================
# fontion qui a donner la distance d'une piece du taquin a ca vrai place
def distance(taquin, piece):
    tacTrie = newTaquin(newlist(len(taquin)), len(taquin))
    position = find(taquin, piece)  # porition=[x,y] de la piece dna le taquin
    xt = position[0]
    yt = position[1]
    position = find(tacTrie, piece)  # position de la piece dans le taquin resolu
    x = position[0]
    y = position[1]
    dist = 0
    if xt != x:
        if xt < x:
            while xt < x:
                xt = xt + 1
                dist = dist + 1
        else:
            while xt > x:
                xt = xt - 1
                dist = dist + 1
    if yt != y:
        if yt < y:
            while yt < y:
                yt = yt + 1
                dist = dist + 1
        else:
            while yt > y:
                yt = yt - 1
                dist = dist + 1
    return dist

# donne liste de mouvments possibles deffectuel pour le taquin
def possibilites(taquin):
    mouves = list()
    if possible(taquin, "H"):
        mouves.append("H")
    if possible(taquin, "B"):
        mouves.append("B")
    if possible(taquin, "D"):
        mouves.append("D")
    if possible(taquin, "G"):
        mouves.append("G")
    return mouves

# retourne la taille de la liste si l'element nest pas de dans et ca place si il exite
def exist(liste, element):
    temp = len(liste)
    i = 0
    found = False
    while found == False and i < len(liste):
        if liste[i] == element and liste[i].f > element.f:
            temp = i
            found == True
        i = i + 1
    return temp

# insere un element dans une liste en la triant
def trieInsert(liste, element):
    if len(liste) == 0:
        liste.append(element)
    else:
        i = 0
        while i < len(liste) and liste[i].f <= element.f:
            i = i + 1

        if i >= len(liste):
            liste.append(element)
        else:
            liste.insert(i, element)

# ========= Arbre de recherche =============
class Noeud:
    def __init__(self, taquin, neudParent, mouvement, profondeur):
        self.taquin = taquin
        self.parent = neudParent
        self.mvm = mouvement
        self.h = 0
        self.g = profondeur
        self.f = 0

    def heuristique(self, k):
        size = (len(self.taquin) * len(self.taquin))
        ct = 0
        p = [4, 1]
        pi = [[0, 36, 12, 12, 4, 1, 1, 4, 1], [0, 8, 7, 6, 5, 4, 3, 2, 1], [0, 8, 7, 6, 5, 4, 3, 2, 1],
              [0, 8, 7, 6, 5, 3, 2, 4, 1], [0, 8, 7, 6, 5, 3, 2, 4, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 36, 35, 34, 33, 12, 12, 16, 4, 8, 1, 1, 4, 1, 2, 7],
              [0, 36, 35, 34, 33, 12, 12, 16, 4, 8, 1, 1, 4, 1, 2, 7]]
        # la valeur de rho est p[k%2]
        for i in range(1, size):
            if i < len(pi[k]):
                # distance de manhatan poondere si le tableau ha des valeurs
                ct = ct + int((distance(self.taquin, i) * pi[k][i]) / p[k % 2])
            elif len(pi[k]) >= size:
                # distance de manhatansimple
                ct = ct + distance(self.taquin, i)
        return ct

    def expanseH(self, k):
        etats = list()
        toDo = possibilites(self.taquin)  # liste des mouvements possibles a faire
        while len(toDo) != 0:  # tant que on a des mouvements a faire
            mvm = toDo.pop(0)  # mvm qu'on est en train de faire
            new = Noeud(bouger(self.taquin, mvm), self, mvm, self.g + 1)
            new.h = new.heuristique(k)
            new.f = new.f + new.h
            etats.append(new)
        return etats

    def __eq__(self, autre):
        if type(self) != type(autre):
            return False
        else:
            return compare(self.taquin, autre.taquin)

    # tranforme le taquin dans l'etat dans un string 
    # pour l'identifier dans un dictionaire
    def toKey(self):
        first = list()
        for i in range(len(self.taquin)):
            first.append("".join(map(str,self.taquin)))
        key="".join(map(str,first))
        return key


def search(start, h):
    a = time.time()  # pour pouvoir afficher le temps d'execution
    frontiere = list()
    visite = {}
    solution = list()  # liste avec les elements de la solution qu'on va renvoye
    objectif = Noeud(newTaquin(newlist(taille), taille), None, "_", 0)  # taquin solution | nottre objectif
    frontiere.append(start)  # add the first state to the fronteer
    arrive = False
    while len(frontiere) != 0 and arrive == False:  # tant que la frotiere n'est pas vide on recherche une solution
        aVisiter = frontiere.pop(0)  # etat qu'on visite
        nEtats = aVisiter.expanseH(h)  # etats possibles
        while len(nEtats) != 0:  # tant que on n'a pas traiete tout les etats generes
            n = nEtats.pop()  # o va decider le destin de ce etat
            if n == objectif:  # soit il est trie et on a trouve notre solution
                objectif = n
                arrive = True
            else:  # soit il ne l'est pas
                # vérifier si n est présent dans visited
                cle = n.toKey()
                if cle in visite:  # si vrai, alors n existe dans visited  et n.f < f dans visited.
                    temp = visite.get(cle)
                    if temp.f > n.f:
                        trieInsert(frontiere, n)
                        del visite[cle]
                else:
                    trieInsert(frontiere, n)
        visite[aVisiter.toKey()]=aVisiter
        b = time.time()
        print("frontiere:", len(frontiere), "||etats visitees:", len(visite), "||\ttemps:", b - a, end="\r")
    print()
    solution.append(objectif)
    t = objectif.parent
    while t.parent is not None:
        solution.insert(0, t)
        t = t.parent
    solution.insert(0, t)
    return solution
