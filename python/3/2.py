


input = open("./3/input.txt","r").read().splitlines()



#oxygen
oxygen = input.copy()
elt_loc = 0

while True:
    if len(oxygen) == 1: break
    val = 0
    
    for elt in oxygen:
        if elt[elt_loc] == "1": val += 1
        if elt[elt_loc] == "0": val -= 1

    for elt in oxygen.copy():
        if val >= 0 and elt[elt_loc] == "0" or \
          val < 0 and elt[elt_loc] == "1": 
          
          oxygen.remove(elt)
    elt_loc += 1

#co2
co2 = input.copy()
elt_loc = 0

while True:
    if len(co2) == 1: break
    val = 0
    
    for elt in co2:
        if elt[elt_loc] == "1": val += 1
        if elt[elt_loc] == "0": val -= 1

    for elt in co2.copy():
        if val >= 0 and elt[elt_loc] == "1" or \
          val < 0 and elt[elt_loc] == "0": 
          
          co2.remove(elt)

    elt_loc += 1


print(oxygen, co2)
print(int(oxygen[0],2)*int(co2[0],2))

# print()

