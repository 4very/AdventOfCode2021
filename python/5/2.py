import re
from pprint import pprint
from typing import overload




input = open("./5/input.txt","r").read().splitlines()

far_r = (0,0)

for i in range(len(input)):
    input[i] = input[i].split(" -> ")
    # split input[i][1] into a pair of ints
    input[i][1] = re.findall(r'\d+', input[i][1])
    input[i][1] = (int(input[i][1][0]), int(input[i][1][1]))
    # split input[i][0] into a pair of ints
    input[i][0] = re.findall(r'\d+', input[i][0])
    input[i][0] = (int(input[i][0][0]), int(input[i][0][1]))

    far_r = (max(far_r[0], input[i][1][0], input[i][0][0]), max(far_r[1], input[i][1][1], input[i][0][1]))

grid = [[0 for i in range(far_r[0]+1)] for j in range(far_r[1]+1)]

for line in input:
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        for i in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0])+1):
            for j in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1])+1):
                grid[i][j] += 1
    
    else:
        # get all of the points in between two diagonal points
        delta = (-1 if line[0][0] > line[1][0] else 1, -1 if line[0][1] > line[1][1] else 1)
        p1 = line[0]
        for i in range(abs(line[0][0]-line[1][0])+1):
            grid[p1[0]][p1[1]] += 1
            p1 = (p1[0]+delta[0], p1[1]+delta[1])
        


overlap = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] > 1: overlap += 1

print(overlap)
# pprint(grid)