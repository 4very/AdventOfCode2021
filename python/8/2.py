import re
from pprint import pprint

def intersection(list1, list2):
    return list(set(list1) & set(list2))

def fivecheck(five, sixlist):
    for elt in sixlist:
        if len(intersection(five, elt)) == 5:
            return True
    return False

input = open("./8/input.txt","r").read().splitlines()

signal = []
output = []
for i in range(len(input)):
    splited = input[i].split(" | ")
    output.append(splited[1].split(" "))

    signals = splited[0].split(" ")
    dic = {i+2:[] for i in range(6)}
    for elt in signals:
        dic[len(elt)].append(elt)
    signal.append(dic.copy())

val = 0
for j in range(len(output)):

    elt = output[j]
    signals = signal[j]
    fourseg = [None, None, None, None]

    for i in range(len(elt)):
        if len(elt[i]) == 2: fourseg[i] = 1
        elif len(elt[i]) == 3: fourseg[i] = 7
        elif len(elt[i]) == 4: fourseg[i] = 4
        elif len(elt[i]) == 5: # 2, 3, and 5 
            if len(intersection(elt[i], signals[3][0])) == 3: fourseg[i] = 3
            elif fivecheck(elt[i],signals[6]): fourseg[i] = 5
            else: fourseg[i] = 2

        elif len(elt[i]) == 6: # 0, 6, and 9
            if len(intersection(elt[i], signals[3][0])) == 2: fourseg[i] = 6
            elif len(intersection(elt[i], signals[4][0])) == 4: fourseg[i] = 9
            else: fourseg[i] = 0

        elif len(elt[i]) == 7: fourseg[i] = 8
    
    val += int("".join([str(int) for int in fourseg]))


print(val)