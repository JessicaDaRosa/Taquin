import numpy as np
import random as rnd
import copy as cp
size = 3
class State:
    def __init__(self, size):
        self.puzzle = np.arange(1 , ((size*size)+1)).reshape(size,size)
        self.puzzle[size-1][size-1] = 0
        self.position = np.argwhere(self.puzzle == 0)
    #tests if the movment is possible
    def possible (self, move): 
        y = self.position[0][0]
        x = self.position[0][1]
        if(move == "U" or move=="u"):
            if y != 0 and y < len(self.puzzle[0]) and y > 0: 
                return True
        elif(move == "D" or move == "d"):
            if y >= 0 and y != (len(self.puzzle[0])-1) and y < len(self.puzzle[0]): 
                return True
        elif move =="R" or move == "r" :
            if x>=0 and x < (len(self.puzzle[0])-1): 
                return True
        elif move == "L" or move == "l":
             if x !=0 and x > 0 and x < len(self.puzzle[0]):
                 return True
        else:
            return False
    #move the empty case to the right
    def mR(self):
        y = self.position[0][0]
        x = self.position[0][1]
        if x>=0 and x<len(self.puzzle[1]) and x != (len(self.puzzle[x])-1):    
            temp = State(len(self.puzzle[x]))
            temp.puzzle = self.puzzle.copy()
            temp.puzzle[y][x]=self.puzzle[y][x+1]
            temp.puzzle[y][x+1]=self.puzzle[y][x]
            temp.position = np.argwhere(temp.puzzle == 0)
            self.puzzle = np.copy(temp.puzzle)
            self.position = temp.position
    #empty case to the left
    def mL(self):
        y = self.position[0][0]
        x = self.position[0][1]
        if x > 0 and x < len(self.puzzle[x]): # x must be bigger than 0 andsmaler that tab.length        
            temp = State(len(self.puzzle[x]))
            temp.puzzle = self.puzzle.copy()
            temp.puzzle[y][x] = self.puzzle[y][x-1]
            temp.puzzle[y][x-1] = self.puzzle[y][x]
            temp.position = np.argwhere(temp.puzzle == 0)
            self.puzzle = np.copy(temp.puzzle)
            self.position = temp.position
    #move up
    def mU (self):
        y = self.position[0][0]
        x = self.position[0][1]
        if y > 0 and y < len(self.puzzle[y]): #y must bebigger that 0  and smaller that tab.length
            temp = State(len(self.puzzle[x]))
            temp.puzzle = self.puzzle.copy()
            temp.puzzle[y][x] = self.puzzle[y-1][x]
            temp.puzzle[y-1][x] = self.puzzle[y][x]
            temp.position = np.argwhere(temp.puzzle == 0)
            self.puzzle = np.copy(temp.puzzle)
            self.position = temp.position
    #alters the current state
    def mD (self):
        y = self.position[0][0]
        x = self.position[0][1]
        if y >= 0 and y < len(self.puzzle[y])-1:   
            temp = State(len(self.puzzle[x]))
            temp.puzzle = self.puzzle.copy()
            temp.puzzle[y][x] = self.puzzle[y+1][x]
            temp.puzzle[y+1][x] = self.puzzle[y][x]
            temp.position=np.argwhere(temp.puzzle == 0)
            self.puzzle = np.copy(temp.puzzle)
            self.position = temp.position
    #returns a move to the right
    def nMR(self):
        temp = State(len(self.puzzle[0]))
        temp.puzzle = self.puzzle.copy()
        temp.mR()
        return temp
    #returns a move to the left
    def nML(self):
        temp = State(len(self.puzzle[0]))
        temp.puzzle = self.puzzle.copy()
        temp.mL()
        return temp
    #returns a move up
    def nMU (self):
        temp = State(len(self.puzzle[0]))
        temp.puzzle = self.puzzle.copy()
        temp.mU()
        return temp
    #returns a movedown
    def nMD (self):
        temp = State(len(self.puzzle[0]))
        temp.puzzle = self.puzzle.copy()
        temp.mD()
        return temp
    # returns a specific mouvement according to what is demanded
    # u : up | d : down | r : right | l : left
    def mouve(self,toDo):
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
    def shuffle(self,number):
        if number == 0: 
            # if the number o mouvements is 0 there is no shuffeling
            return self
        else:
            for ct in  range(number) :
                # while the nuber of mouvment isn't done we are going to randomly chose a mouvment 
                # and check ifwe can do it 
                # if we can we will if not another one will be generated 
                mvm = rnd.choice("UDRL")
                if self.possible(mvm)!=True or self.possible(mvm)==False:
                    while self.possible(mvm)!=True :
                        mvm = rnd.choice("UDRL")
                if mvm == "U":
                    self.mU()
                if mvm =="D":
                    self.mD()
                if mvm == "R":
                    self.mR()
                if mvm == "L":
                    self.mL()
    # returns de distance of a character from its actual possition  to 
    # the goal position
    def distance (self,character):
        goal = State(len(self.puzzle[0])).puzzle
        goalP = np.argwhere(goal == character)[0]
        position = np.argwhere(self.puzzle == character)[0]
        dist = 0
        if position[0] != goalP[0]:
            if position [0] > goalP[0] :
                while position [0] != goalP[0]:
                    position[0] = position[0]-1
                    dist = dist +1
            elif position[0] < goalP[0]:
                while position[0] != goalP[0]:
                    position[0] = position[0] +1
                    dist = dist+1
        if position[1] != goalP[1]:
            if  position[1] > goalP[1]:
                while position[1] != goalP[1]:
                    position[1] =position[1] -1
                    dist = dist+1
            elif position[1] < goalP[1]:
                while position[1] != goalP[1]:
                    position[1] = position[1] +1
                    dist = dist + 1
        return dist
    # returns a list of Trues and Falses
    # True if the element is at it's place
    # False if not
    def positions (self):
        m = list()
        position = [0,0]
        goal = State(len(self.puzzle[0])).puzzle
        for y in range(0,(len(self.puzzle[0]))):
            position [0]=y
            for x in range (0,(len(self.puzzle[0]))):
                position[1]=x
                if self.puzzle[y][x]==goal[y][x]:
                    m.append(True)
                else:
                    m.append(False)
        return m
    # returns the number of falses in the abose function positions
    def nbPieces(self):
        thing = self.positions()
        counter = 0
        for x in range(len(thing)):
            if thing[x] == False :
                counter = counter +1
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
    def compare(self,other):
        result = True
        if len(self.puzzle[0])!=len(other.puzzle[0]) :
            result = False
        else:
            for y in range(len(self.puzzle[0])):
                for x in range(len(self.puzzle[0])):
                    if self.puzzle[y][x]!=other.puzzle[y][x]:
                        result = False
            return result
                            
temp = State(size)
temp.shuffle(50)
print(temp.puzzle,"\n")
temp.positions()

class Noeud :
    def __init__(self, stateFather,stateSon,distance,heuristic):
        self.son = stateSon
        self.father = stateFather
        self.h = heuristic
        self.g = distance
        self.f =self.h +self.g
    # expanses using the number os misplaced pieces as an heuristic
    def expansePieces(self):
        fronteer = list()
        toDo = self.son.possibilities()
        while len(toDo) != 0:
            doing = toDo.pop(0)
            new = Noeud(self,self.son.mouve(doing),self.g+1,0)
            new.h = new.son.nbPieces()
            fronteer.append(new)
        return fronteer
    # expanses usinf the manhatan distance as an heuristic 
    def expanseManhatan(self):
        fronteer = list()
        toDo = self.son.possibilities()
        while len(toDo) != 0:
            doing = toDo.pop(0)
            new = Noeud(self,self.son.mouve(doing),self.g+1,0)
            new.h=new.manhatan()
            print(new.h)
            fronteer.append(new)
        return fronteer
    #calculates the manhatan distance for the guiven puzzle
    def manhatan(self):
        ct = 0
        for i in range(0,(len(self.son.puzzle[0])*len(self.son.puzzle[0]))):
            ct = ct + self.son.distance(i)
        return ct
    #true if the 2 have te same puzzle
    def compare(self,other):
        return self.son.compare(other.son)

#orders a list os Noeuds by their f

no = Noeud(None,temp,0,0)
no2 = no.expanseManhatan()[0]
print(no.son.puzzle,"no\n\n",no2.son.puzzle,"no2\n",no.compare(no2),"\n")

thing = no2.expanseManhatan()
for i in range(len(thing)):
    print(thing[i].son.puzzle,"\t",thing[i].h)
