import re
from pprint import pprint


input = open("./8/input.txt","r").read().splitlines()

signal = []
output = []
for i in range(len(input)):
    splited = input[i].split(" | ")
    signal.append(splited[0].split(" "))
    output.append(splited[1].split(" "))

print(signal)
print(output)

val = 0
for elt in output:
    for i in range(len(elt)):
        if len(elt[i]) == 2 or \
           len(elt[i]) == 3 or \
           len(elt[i]) == 4 or \
           len(elt[i]) == 7:
            val += 1


print(val)