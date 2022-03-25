


input = open("./3/input.txt","r").read().splitlines()


gamma = [0 for i in range(len(input[0]))]

for elt in input:
    for i in range(len(elt)):
        if elt[i] == "1": gamma[i] += 1
        if elt[i] == "0": gamma[i] -= 1
        
gamma_b = "".join(["0" if i < 0 else "1" for i in gamma])
ep_b = "".join(["0" if i > 0 else "1" for i in gamma])

print(int(gamma_b,2)*int(ep_b,2))

# print()

