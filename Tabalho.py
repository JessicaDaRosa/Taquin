import state as node
import s1 as s1
import time
size = 3

n = 40

temp = node.State(size)# creating a solved puzzle
goal = node.Node(None, temp, 0, "_")# creating a goal node
temp.shuffle(n)# shuffeling the goal node
start = node.Node(None, temp, 0, "fuck")# creating a neu node with a shuffled puzzle

h = 0
print("__________________________h1___________________________")
s = time.time()
solution = s1.search(start, h)
end = time.time()
print(start.son.puzzle, "start\n")
for i in range(1, len(solution)):
    print(solution[i].son.puzzle, solution[i].mvm, solution[i].g, solution[i].f, "\n")
d = end - s
print(d)

h = 1
print("__________________________h2___________________________")
s = time.time()
solution = s1.search(start, h)
end = time.time()
print(start.son.puzzle, "start\n")
for i in range(1, len(solution)):
    print(solution[i].son.puzzle, solution[i].mvm, solution[i].g, solution[i].f, "\n")
d = end - s
print(d)

h = 3
print("__________________________h3___________________________")
s = time.time()
solution = s1.search(start, h)
end = time.time()
print(start.son.puzzle, "start\n")
for i in range(1, len(solution)):
    print(solution[i].son.puzzle, solution[i].mvm, solution[i].g, solution[i].f, "\n")
d = end - s
print(d)

h = 4
print("__________________________h5___________________________")
s = time.time()
solution = s1.search(start, h)
end = time.time()
print(start.son.puzzle, "start\n")
for i in range(1, len(solution)):
    print(solution[i].son.puzzle, solution[i].mvm, solution[i].g, solution[i].f, "\n")
d = end - s
print(d)

h = 5
print("__________________________h6___________________________")
s = time.time()
solution = s1.search(start, h)
end = time.time()
print(start.son.puzzle, "start\n")
for i in range(1, len(solution)):
    print(solution[i].son.puzzle, solution[i].mvm, solution[i].g, solution[i].f, "\n")
d = end - s
print(d)