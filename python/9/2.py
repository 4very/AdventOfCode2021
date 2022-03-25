import re
from pprint import pprint
from random import choice
from math import prod

def lowest(point, neighbors, valdict):
    for elt in neighbors:
        if valdict[elt] <= valdict[point]:
            return False
    return True


input = open("./9/input.txt","r").read().splitlines()

# random unexplored point
# depth first search then add all visited to a list
# all greater values surrounding point cannot be low, so also add those


# pprint(input)

# (0,0): 0
# (0,0): [(0,1), (1,0)]

vals = {}
neigh = {}
for row in range(len(input)):
    for col in range(len(input[row])):
        vals[(row, col)] = int(input[row][col])
        tlist = []
        
        if row > 0: tlist.append((row-1, col))
        if row < len(input)-1: tlist.append((row+1, col))
        if col > 0: tlist.append((row, col-1))
        if col < len(input[row])-1: tlist.append((row, col+1))

        neigh[(row, col)] = tlist.copy()

to_visit = list(vals.keys())
queue = [choice(to_visit)]
to_visit.remove(queue[0])
low = []
group = 0

while len(to_visit) > 0:
    if len(queue) == 0:
        if group != 0:
            low.append(group)
        group = 0
        rand = choice(to_visit)
        queue.append(rand)
        to_visit.remove(rand)

    
    point = queue.pop(0)
    if vals[point] == 9: continue
    group += 1

    for neighbor in neigh[point]:
        if vals[neighbor] == 9: continue
        if neighbor in to_visit:
            queue.append(neighbor)
            to_visit.remove(neighbor)


print(prod(sorted(low, reverse=True)[:3]))