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

dic = {i:fish.count(i) for i in set(fish)}
for i in range(-1,10):
    if i not in dic:
        dic[i] = 0
pprint(dic, width=1)

for i in range(256):
    # print("day", i)
    # pprint(dic,width=1)
    # print("-------")
    tdic = {i:0 for i in range(-1,10)}
    for key, val in dic.items():
        if val != 0:
            tdic[key-1] = val
    
    tdic[6] += tdic[-1]
    tdic[8] += tdic[-1]
    tdic[-1] = 0
    dic = tdic.copy()

print(sum(dic.values()))
