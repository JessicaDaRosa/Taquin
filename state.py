import numpy as np
import random as rnd
import copy as cp


class State:
    def __init__(self, size):
        self.puzzle = np.arange(1, ((size * size) + 1)).reshape(size, size)
        self.puzzle[size - 1][size - 1] = 0

    # tests if the movment is possible
    def possible(self, move):
        position = np.argwhere(self.puzzle == 0)[0]
        if move == "U" or move == "u":
            if position[0] != 0 and position[0] < len(self.puzzle[0]) and position[0] > 0:
                return True
        elif move == "D" or move == "d":
            if position[0] >= 0 and position[0] != (len(self.puzzle[0]) - 1) and position[0] < len(self.puzzle[0]):
                return True
        elif move == "R" or move == "r":
            if position[1] >= 0 and position[1] < (len(self.puzzle[0]) - 1):
                return True
        elif move == "L" or move == "l":
            if position[1] != 0 and position[1] > 0 and position[1] < len(self.puzzle[0]):
                return True
        else:
            return False

    # move the empty case to the right
    def mR(self):
        position = np.argwhere(self.puzzle == 0)[0]
        if position[1] >= 0 and position[1] < len(self.puzzle[0]) - 1 and position[1] != (
                len(self.puzzle[position[1]]) - 1):
            temp = State(len(self.puzzle[position[1]]))
            temp.puzzle = self.puzzle.copy()
            temp.puzzle[position[0]][position[1]] = self.puzzle[position[0]][position[1] + 1]
            temp.puzzle[position[0]][position[1] + 1] = self.puzzle[position[0]][position[1]]
            self.puzzle = np.copy(temp.puzzle)

    # empty case to the left
    def mL(self):
        position = np.argwhere(self.puzzle == 0)[0]
        if position[1] > 0 and position[1] < len(
                self.puzzle[position[1]]):  # x must be bigger than 0 andsmaler that tab.length
            temp = State(len(self.puzzle[position[1]]))
            temp.puzzle = self.puzzle.copy()
            temp.puzzle[position[0]][position[1]] = self.puzzle[position[0]][position[1] - 1]
            temp.puzzle[position[0]][position[1] - 1] = self.puzzle[position[0]][position[1]]
            self.puzzle = np.copy(temp.puzzle)

    # move up
    def mU(self):
        position = np.argwhere(self.puzzle == 0)[0]
        if position[0] > 0 and position[0] < len(
                self.puzzle[position[0]]):  # y must bebigger that 0  and smaller that tab.length
            temp = State(len(self.puzzle[position[0]]))
            temp.puzzle = self.puzzle.copy()
            temp.puzzle[position[0]][position[1]] = self.puzzle[position[0] - 1][position[1]]
            temp.puzzle[position[0] - 1][position[1]] = self.puzzle[position[0]][position[1]]
            self.puzzle = np.copy(temp.puzzle)

    # alters the current state
    def mD(self):
        position = np.argwhere(self.puzzle == 0)[0]
        if position[0] >= 0 and position[0] < len(self.puzzle[position[0]]) - 1:
            temp = State(len(self.puzzle[position[1]]))
            temp.puzzle = self.puzzle.copy()
            temp.puzzle[position[0]][position[1]] = self.puzzle[position[0] + 1][position[1]]
            temp.puzzle[position[0] + 1][position[1]] = self.puzzle[position[0]][position[1]]
            self.puzzle = np.copy(temp.puzzle)

    # returns a specific mouvement according to what is demanded
    # u : up | d : down | r : right | l : left
    def mouve(self, toDo):
        goal = cp.copy(self)
        if toDo == "u" or toDo == "U":
            goal.mU()
        elif toDo == "d" or toDo == "D":
            goal.mD()
        elif toDo == "r" or toDo == "R":
            goal.mR()
        elif toDo == "l" or toDo == "L":
            goal.mL()
        return goal

    # returns a shufled puzzle
    def shuffle(self, number):
        if number == 0:
            # if the number o mouvements is 0 there is no shuffeling
            return self
        else:
            for ct in range(number):
                # while the nuber of mouvment isn't done we are going to randomly chose a mouvment 
                # and check ifwe can do it 
                # if we can we will if not another one will be generated 
                mvm = rnd.choice("UDRL")
                if self.possible(mvm) != True or self.possible(mvm) == False:
                    while self.possible(mvm) != True:
                        mvm = rnd.choice("UDRL")
                if mvm == "U":
                    self.mU()
                if mvm == "D":
                    self.mD()
                if mvm == "R":
                    self.mR()
                if mvm == "L":
                    self.mL()

    # returns de distance of a character from its actual possition  to
    # the goal position
    def distance(self, character):
        goal = State(len(self.puzzle[0])).puzzle
        goalP = np.argwhere(goal == character)[0]
        position = np.argwhere(self.puzzle == character)[0]
        dist = 0
        if position[0] != goalP[0]:
            if position[0] > goalP[0]:
                while position[0] != goalP[0]:
                    position[0] = position[0] - 1
                    dist = dist + 1
            elif position[0] < goalP[0]:
                while position[0] != goalP[0]:
                    position[0] = position[0] + 1
                    dist = dist + 1
        if position[1] != goalP[1]:
            if position[1] > goalP[1]:
                while position[1] != goalP[1]:
                    position[1] = position[1] - 1
                    dist = dist + 1
            elif position[1] < goalP[1]:
                while position[1] != goalP[1]:
                    position[1] = position[1] + 1
                    dist = dist + 1
        return dist

    # returns a list of Trues and Falses
    # True if the element is at it's place
    # False if not
    def positions(self):
        m = list()
        goal = State(len(self.puzzle[0])).puzzle
        for y in range(0, (len(self.puzzle[0]))):
            for x in range(0, (len(self.puzzle[0]))):
                if self.puzzle[y][x] == goal[y][x]:
                    m.append(True)
                else:
                    m.append(False)
        return m

    # returns the number of falses in the abose function positions
    def nbPieces(self):
        thing = self.positions()
        counter = 0
        for x in range(len(thing)):
            if thing[x] == False:
                counter = counter + 1
        return counter

    # returns a list of possible mouvments
    def possibilities(self):
        mouves = list()
        if self.possible("U"):
            mouves.append("U")
        if self.possible("D"):
            mouves.append("D")
        if self.possible("R"):
            mouves.append("R")
        if self.possible("L"):
            mouves.append("L")
        return mouves

    def __eq__(self, value):
        result = True
        if len(self.puzzle[0]) != len(value.puzzle[0]):
            result = False
        else:
            for y in range(len(self.puzzle[0])):
                for x in range(len(self.puzzle[0])):
                    if self.puzzle[y][x] != value.puzzle[y][x]:
                        result = False
            return result

    def __str__(self):
        return print(self.puzzle)


class Node:
    def __init__(self, stateFather, stateSon, distance, movment):
        self.son = stateSon
        self.father = stateFather
        self.h = 0
        self.g = distance
        self.f = distance
        self.mvm = movment

    # expanses using the number os misplaced pieces as an heuristic
    def expansePieces(self):
        fronteer = list()
        toDo = self.son.possibilities()
        while len(toDo) != 0:
            doing = toDo.pop(0)
            new = Node(self, self.son.mouve(doing), self.g + 1, doing)
            new.h = new.son.nbPieces()
            new.f = new.f + new.h
            fronteer.append(new)
        return fronteer

    # expanses usinf the manhatan distance as an heuristic
    def expanseH(self, k):
        fronteer = list()
        toDo = self.son.possibilities()
        while len(toDo) != 0:
            doing = toDo.pop(0)
            new = Node(self, self.son.mouve(doing), self.g + 1, doing)
            new.h = new.heuristique(k)
            new.f = new.f + new.h
            fronteer.append(new)
        return fronteer

    def heuristique(self, k):
        size = (len(self.son.puzzle[0]) * len(self.son.puzzle[0]))
        ct = 0
        p = [4, 1]
        pi = [[0, 36, 12, 12, 4, 1, 1, 4, 1], [0, 8, 7, 6, 5, 4, 3, 2, 1], [0, 8, 7, 6, 5, 4, 3, 2, 1],
              [0, 8, 7, 6, 5, 3, 2, 4, 1], [0, 8, 7, 6, 5, 3, 2, 4, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 36, 35, 34, 33, 12, 12,16, 4, 8 , 1, 1, 4, 1,2,7],[0, 36, 35, 34, 33, 12, 12,16, 4, 8 , 1, 1, 4, 1, 2, 7]]
        # the value of p used is p[k%2]
        for i in range(1, size):
            if i < len(pi[k]):
                # distance de manhatan poondere si le tableau ha des valeurs 
                ct = ct + int((self.son.distance(i) * pi[k][i]) / p[k % 2])
            elif len(pi[k]) >= size:
                # distance de manhatansimple
                ct = ct + self.son.distance(i)
        return ct
        # true if the 2 have te same puzzle

    def __eq__(self, value):
        if value != None:
            return self.son == value.son
        else:
            return False

    def __str__(self):
        return print(self.son)
