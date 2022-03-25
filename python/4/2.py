import re
from pprint import pprint

def rws(input):
    # remove leading whitespace
    input = re.sub(r"^\s+", "", input)
    # replace consecutive whitespace with a single space
    return re.sub(r'\s+', ' ', input)


def restructure(board):
    ret = [["-" for _ in range(5)] for _ in range(5)]
    for key, val in board.items():
        ret[val[0]-1][val[1]-1] = key
    
    pprint(ret)



input = open("./4/input.txt","r").read().splitlines()

numbers = input[0].split(",")
# convert all numbers to ints
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# list of list for each row on board


# list of dict where each number on the bingo board is a cordinate to its spot on the board
boards = []
for i in range(2,len(input), 6):
    boards.append({})
    for j in range(5):
        input[i+j] = rws(input[i+j]).split(" ")
        for z in range(5):
            boards[-1][int(input[i+j][z])] = (j+1,z+1)


#    1  2  3  4  5
# 1 22 13 17 11  0
# 2 8  2 23  4 24
# 3 21  9 14 16  7
# 4 6 10  3 18  5
# 5 1 12 20 15 19
temp = {}
for i in range(5):
    temp[(i+1,0)] = 0
    temp[(0,i+1)] = 0
    
scores = [temp.copy() for i in range(len(boards))]
wins = [0 for i in range(len(boards))]

for elt in numbers:
    for i in range(len(boards)):
        if elt in boards[i]:
            square = boards[i][elt]
            del boards[i][elt]

            scores[i][(square[0],0)] += 1
            scores[i][(0,square[1])] += 1

            if scores[i][(square[0],0)] == 5 or \
               scores[i][(0,square[1])] == 5:

                wins[i] = 1

               # check if list wins only has one occurance of a number
                # if so, then that number is the winner
                if len(set(wins)) == 1:
                    print(sum(boards[i].keys())* elt)
                    break



# pprint(scores)
