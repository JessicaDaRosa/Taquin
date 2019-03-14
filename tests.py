import state 
size = 3
k = 3
temp = state.State(size)
temp.shuffle(50)
print(temp.puzzle," temp \n")
temp.positions()

no = state.Node(None,temp,0)
no2 = no.expanseH(1)[0]
print(no.son.puzzle,"no == temp\n")
print(no2.son.puzzle,"no2")
thing = no2.expanseH(k)
for i in range(len(thing)):
    print("\n",thing[i].son.puzzle,"\t","f:",thing[i].f,"g:",thing[i].g,"h:",thing[i].h)
