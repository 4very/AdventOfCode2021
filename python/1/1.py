


input = open("./1/input.txt","r").read().splitlines()

ret = 0


for i in range(1,len(input)):
    if int(input[i]) > int(input[i-1]): ret += 1

print(ret)
