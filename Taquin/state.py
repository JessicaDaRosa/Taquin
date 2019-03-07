import numpy as np
import random as rnd
size = 3
class State:
    def __init__(self, size):
        self.puzzle = np.arange(1 , ((size*size)+1)).reshape(size,size)
        self.puzzle[size-1][size-1] = 0
        self.position = np.argwhere(self.puzzle == 0)

    def possible (self, move): #tests if the movment is possible
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
    def mR(self):#move the empty case to the right
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
    def mL(self):#empty case to the left
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
    def mU (self):#move up
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
    def mD (self):#alters the current state
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
    def nMR(self):#returns a move to the right
        temp = State(len(self.puzzle[0]))
        temp.puzzle = self.puzzle.copy()
        temp.mR()
        return temp
    def nML(self):#returns a move to the left
        temp = State(len(self.puzzle[0]))
        temp.puzzle = self.puzzle.copy()
        temp.mL()
        return temp
    def nMU (self):#returns a move up
        temp = State(len(self.puzzle[0]))
        temp.puzzle = self.puzzle.copy()
        temp.mU()
        return temp
    def nMD (self):#returns a movedown
        temp = State(len(self.puzzle[0]))
        temp.puzzle = self.puzzle.copy()
        temp.mD()
        return temp
    def shuffle(self,number):
        if number == 0: 
            return self
        else:
            for ct in  range(number) :
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
                    


temp = State(size)
temp.shuffle(200)
print (temp.puzzle)


