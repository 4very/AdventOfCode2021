


input = open("./2/input.txt","r").read().splitlines()
for i in range(len(input)):
    
    input[i] = input[i].split(" ")
    input[i][1] = int(input[i][1])

horiz = 0
depth = 0
aim = 0

for elt in input:
    if elt[0] == "forward": 
        horiz += elt[1]
        depth += aim * elt[1]
    if elt[0] == "down": aim += elt[1]
    if elt[0] == "up": aim -= elt[1]

print(horiz*depth)
