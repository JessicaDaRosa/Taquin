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
            if y > 0 and y < len(self.puzzle[y])-1: 
                return True
        elif(move == "D" or move == "d"):
            if y >= 0 and y < (len(self.puzzle[y])-1): 
                return True
        elif move =="R" or move == "r" :
            if x>=0 and x<len(self.puzzle[1]) and x != len(self.puzzle[x])-1: 
                return True
        elif move == "L" or move == "l":
             if x > 0 and x < len(self.puzzle[x])-1:
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
            temp = State(len(self.puzzle[0]))
            temp.puzzle = self.puzzle.copy()
            for ct in  range(number) :
                mvm = rnd.choice("UDRL")
                if self.possible(mvm)!=True:
                    while self.possible(mvm)!=True :
                        print ("\t",mvm)
                        mvm = rnd.choice("UDRL")
                print (mvm, self.possible(mvm))
                if mvm == "U":
                    temp.mU()
                if mvm =="D":
                    temp.mD()
                if mvm == "R":
                    temp.mR()
                if mvm == "L":
                    temp.mL()
                print (temp.puzzle)
            return temp
                    


temp = State(size)
temp.shuffle(5)


