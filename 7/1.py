import re
from pprint import pprint

def calmoves(list, spot):
    sum = 0
    for elt in list:
        # print(elt, "to", spot, "=", sigma(abs(elt-spot)+1))
        sum += abs(elt-spot)
    return int(sum)

def median(list):
    list.sort()
    if len(list) % 2 == 0:
        return (list[int(len(list)/2)] + list[int(len(list)/2)-1])/2
    else:
        return list[int(len(list)/2)]

input = open("./7/input.txt","r").read().splitlines()

crabs = input[0].split(",")
for i in range(len(crabs)): crabs[i] = int(crabs[i])


print(calmoves(crabs, median(crabs)))