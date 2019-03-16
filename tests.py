import state as node
import numpy as np
import search
size = 5
n = 10
h = 4
temp = node.State(size)# creating a solved puzzle
goal = node.Node(None,temp,0,"_")# creating a goal node
temp.shuffle(n)# shuffeling the goal node
start = node.Node(None,temp,0,"fuck")# creating a neu node with a shuffled puzzle
print(start.son.puzzle,"start\n")
solution = search.search(start,h)
#for i in range (len(solution[0])):
#    print(solution[0][i])
for i in range(1,len(solution)):
    print(solution[i].son.puzzle,solution[i].mvm,"\n")
