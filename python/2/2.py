


input = open("./2/input.txt","r").read().splitlines()
for i in range(len(input)):
    
    input[i] = input[i].split(" ")
    input[i][1] = int(input[i][1])

ret = 0
first = [input[0],input[1],input[2]]
second = [input[1],input[2],input[3]]

for i in range(5,len(input)):
    # print("first:", first, sum(first))
    # print("second:", second, sum(second), "\n")
    if sum(second) > sum(first): ret += 1

    first = second.copy()
    second.pop(0)
    second.append(input[i])


    

print(ret)
