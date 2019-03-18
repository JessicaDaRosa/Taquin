import state as node
import copy as cp

def exist(list, element):
	temp = len(list)
	i=0
	found = False
	while found == False and i <len(list):
		if list[i] == element:
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
				# n existe dans la frontiere
				y = exist(fronteer,n)
				if y < len(fronteer)  and fronteer[x].f > n.f: # vrai si y < len(frontiere), n existe deja
					fronteer.pop(y) # on eleve n de la frontiere
					TrieInsert(fronteer,n)# on ajoute le nouveau n a la forntiere	
				 #vérifier si n est présent dans visited
				# n a deja etait visite
				x = exist(visited, n)
				if x < len(visited) and visited[x].f > n.f : #si vrai, alors n existe dans visited  et n.f < f dans visited.
					visited.pop(x) # on eleve n de visited
					TrieInsert(fronteer, n) # on ajoute n a la frontiere
				if y >= len(fronteer) and x>=len(visited):
					TrieInsert(fronteer,n)
		TrieInsert(visited, aVisiter)
	solution.append(goal)
	t = goal.father
	while t.father != None:
		solution.insert(0,t)
		t = t.father
	solution.insert(0,t)
	return solution
