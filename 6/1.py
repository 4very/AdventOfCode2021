import re
from pprint import pprint

def minus(list):
    # subtrack one from every fish
    for j in range(len(fish)):
        fish[j] = int(fish[j]) - 1
    return fish


input = open("./6/input.txt","r").read().splitlines()

fish = input[0].split(",")
for i in range(len(fish)): fish[i] = int(fish[i])

for i in range(79):
    fish = minus(fish)
    for j in range(len(fish)):
        if fish[j] == 0:
            fish[j] = 7
            fish.append(9)

print(len(fish))
