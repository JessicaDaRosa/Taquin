import state as node
import s1 as s1
import time

size = 3
h = 3
n = 25

temp = node.State(size)  # creating a solved puzzle
# ------------ nxn random
#temp.shuffle(n)# shuffeling the node
# ------------ taquin test 1
# ------------ 3x3
temp.puzzle = node.np.array([2, 8, 4, 1, 6, 3, 7, 5, 0]).reshape(size, size)

# taquin test 2 3x3
# temp.puzzle = node.np.array([1, 6, 2, 7, 0, 3, 5, 4, 8]).reshape(size,size)

#taquin test 3 4x4
#temp.puzzle = node.np.array([[ 6,1,3,4], [ 0,  5,  7,  8], [13,  2, 10, 11], [14,  9, 15, 12]])

start = node.Node(None, temp, 0, "fuck")  # creating a neu node with a shuffled puzzle
print(start.son.puzzle, "start\n")

s = time.time()
solution = s1.search(start, h)
end = time.time()
thing = list()
for i in range(1, len(solution)):
    thing.append(solution[i].mvm)
#    print(solution[i].son.puzzle, "movement", solution[i].mvm, " h:", solution[i].h, " g:", solution[i].g, " f:",
#         solution[i].f, "\n")

print(thing,len(solution)-1)
d = end - s
print("temps ecoule:", d)
