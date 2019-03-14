import state as node
import copy as cp
size = 3
n = 50
h = 1
fronteer = list()
visited = list()
temp = node.State(size)# creating a solved puzzle
goal = node.Node(None,temp,0)# creating a goal node
temp.shuffle(n)# shuffeling the goal node
start = node.Node(None,temp,0)# creating a neu node with a shuffled puzzle
fronteer.append(start) # add the first state to the fronteer
foundIt = False

while len(fronteer)!= 0 and foundIt == False:
    if len(fronteer) == 1:
        father = fronteer.pop()
    elif len(fronteer) > 1:
        father = fronteer.pop()
        for i in range(len(fronteer)):
            if father.f > fronteer[i].f<i:
                fronteer.append
print (goal.son.puzzle)
print(temp.puzzle)