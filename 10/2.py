import re
from pprint import pprint
from random import choice
from statistics import median



input = open("./10/input.txt","r").read().splitlines()

score = []
scores = {
    ")" : 1,
    "}" : 3,
    "]" : 2,
    ">" : 4,
}

for line in input:
    closures = []
    for char in line:
        if char == "(": closures.append(")")
        elif char == "[": closures.append("]")
        elif char == "{": closures.append("}")
        elif char == "<": closures.append(">")
        else:
            exp = closures.pop()
            if char != exp:
                closures = []
                break

    if closures != []:
        print(closures[::-1])
        tmp_score = 0
        for char in closures[::-1]:
            tmp_score *= 5
            tmp_score += scores[char]
        score.append(tmp_score)





print(score)  
print(median(score))