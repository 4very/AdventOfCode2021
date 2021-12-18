import re
from pprint import pprint
from random import choice



input = open("./10/input.txt","r").read().splitlines()

closures = []
score = 0
scores = {
    ")" : 3,
    "}" : 1197,
    "]" : 57,
    ">" : 25137,
}

for line in input:
    for char in line:
        if char == "(": closures.append(")")
        elif char == "[": closures.append("]")
        elif char == "{": closures.append("}")
        elif char == "<": closures.append(">")
        else:
            exp = closures.pop()
            if char != exp:
                # print("expected", exp, "but found", char, "instead")
                score += scores[char]
                break

        
            
print(score)