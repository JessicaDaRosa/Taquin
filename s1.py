import state as node
import copy as cp
import time 

def exist(list, element):
	temp = len(list)
	i=0
	found = False
	while found == False and i <len(list):
		if list[i].son == element.son and list[i].f > element.f:
			temp = i
			found == True
		i = i+1
	return temp

def TrieInsert(list,element):
	if len(list)==0:
		list.append(element)
	else:
		i=0
		while i < len(list) and list[i].f <= element.f:
			i=i+1

		if i >= len(list):
			list.append(element)
		else:
			list.insert(i,element)

def search(start, h):
	a = time.time()
	fronteer = list()
	visited = list()
	solution = list()
	temp = node.State(len(start.son.puzzle[0]))# creating a solved puzzle
	goal = node.Node(None,temp,0,"_")# creating a goal node
	fronteer.append(start) # add the first state to the fronteer
	foundIt = False
	while len(fronteer)!=0 and foundIt==False:
		aVisiter = fronteer.pop(0)
		nEtats = aVisiter.expanseH(h)
		while len(nEtats)!=0:
			n = nEtats.pop()
			if n == goal:
					goal = n
					foundIt = True
			else:
				y = exist(fronteer,n)
				x = exist(visited, n)
				if y < len(fronteer) : #si vrai, alors n existe dans la frontière et n.f < f dans frontière.
					fronteer.pop(y)
					TrieInsert(fronteer,n)
				 #vérifier si n est présent dans visited
				elif x < len(visited) : #si vrai, alors n existe dans visited  et n.f < f dans visited.
					TrieInsert(fronteer, n)
					visited.pop(x)
				elif y == len(fronteer) and x == len(visited):
					TrieInsert(fronteer,n)
		TrieInsert(visited, aVisiter)
		b=time.time()
		print("frontear:",len(fronteer),"visited:",len(visited),"gmin:",fronteer[0].g,"\t",b-a,end="\r")
	print()
	solution.append(goal)
	t = goal.father
	while t.father != None:
		solution.insert(0,t)
		t = t.father
	solution.insert(0,t)
	return solution
