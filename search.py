import taquin as node
import copy as cp
size = 3
n = 50
h = 1
temp = node.State(size)# creating a solved puzzle
goal = node.Node(None,temp,0)# creating a goal node
temp.shuffle(n)# shuffeling the goal node
start = node.Node(None,temp,0)# creating a neu node with a shuffled puzzle


def min():
	position=0
	min=global.fronteer[0].f
	for i in xrange(1, len(global.fronteer)):
		if(global.fronteer[i].f<min):
			min=global.fronteer[i].f
			position=i
	return position

def exist(list, element):
	temp = len(list)
	for x in xrange(len(list)):
		if list[i]==element and list[i].f > element.f:
			temp = i
	return temp

def search(self, start, h):
	fronteer = list()
	visited = list()
	temp = node.State(size)# creating a solved puzzle
	goal = node.Node(None,temp,0)# creating a goal node
	fronteer.append(start) # add the first state to the fronteer
	foundIt = False
	while len(fronteer)!=0 and foundIt==False:
		aVisiter = fronteer.pop(global.min())
		nEtats = aVisiter.expanseH(h)
		while len(nEtats)!=0:
			n = nEtats.pop()
			x = exist(fronteer, n)
			if x < len(fronteer) : #si vrai, alors n existe dans la frontière et n.f < f dans frontière.
				fronteer.append(n)
				fronteer.pop(x)
			else : #vérifier si n est présent dans visited
				x = exist(visited, n)
				if x < len(visited) : #si vrai, alors n existe dans visited  et n.f < f dans visited.
					fronteer.append(n)
					visited.pop(x)
				elif n == goal:
					goal = n
					foundIt = True
				else: 
					fronteer.append(n)