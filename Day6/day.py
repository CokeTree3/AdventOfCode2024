with open('input.txt', 'r') as file:
    inp = file.readlines()
    data = [list(line.strip()) for line in inp]

guard = (0,0, 'v')
for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '^' :
                guard = (i,j, '^')
                print(guard)
                break


def half_1(guard):
    moves = 0
    while(True):
        
        if guard[2] == '^':
            (nextX, nextY) = (guard[0] - 1, guard[1])
            if(nextX == -1):
                data[guard[0]][guard[1]] = 'X'
                moves += 1
                break
            if(data[nextX][nextY] == '#'):
                guard = (guard[0], guard[1], '>')
            else:
                if(data[guard[0]][guard[1]] != 'X'):
                    moves += 1
                data[guard[0]][guard[1]] = 'X'
                guard = (nextX, nextY, '^')        
                

        elif guard[2] == '>':
            (nextX, nextY) = (guard[0], guard[1] + 1)
            if nextY == len(data[0]):
                data[guard[0]][guard[1]] = 'X'
                moves += 1
                break
            if(data[nextX][nextY] == '#'):
                guard = (guard[0], guard[1], 'v')
            else:
                if(data[guard[0]][guard[1]] != 'X'):
                    moves += 1
                data[guard[0]][guard[1]] = 'X'
                guard = (nextX, nextY, '>')

        elif guard[2] == 'v':
            (nextX, nextY) = (guard[0] + 1, guard[1])
            if nextX == len(data):
                data[guard[0]][guard[1]] = 'X'
                moves += 1
                break
            if(data[nextX][nextY] == '#'):
                guard = (guard[0], guard[1], '<')
            else:
                if(data[guard[0]][guard[1]] != 'X'):
                    moves += 1
                data[guard[0]][guard[1]] = 'X'
                guard = (nextX, nextY, 'v')

        elif guard[2] == '<':
            (nextX, nextY) = (guard[0], guard[1] - 1)
            if nextY == -1:
                data[guard[0]][guard[1]] = 'X'
                moves += 1
                break
            if(data[nextX][nextY] == '#'):
                guard = (guard[0], guard[1], '^')
            else:
                if(data[guard[0]][guard[1]] != 'X'):
                    moves += 1
                data[guard[0]][guard[1]] = 'X'
                guard = (nextX, nextY, '<')
        else:
            print("\n\n bad\n\n")
            break
    for line in data:
        print(line)
    return moves

print("Answer to Part 1:", half_1(guard))
print()
#print("Answer to Part 2:", half_2())
















'''
inpFile = open("input.txt", "r")
inp = inpFile.readlines()

directions = list(inp[0].strip())

nodeList =  getNodeList(inp[2:len(inp)])

dirKey = {"R": 1, "L": 0}

curDirectionIndx = 0
step = 0

curNode = "AAA"
while(curNode != "ZZZ"):
    
    nextNode = nodeList[curNode][dirKey[directions[curDirectionIndx]]]
    curDirectionIndx += 1
    if(curDirectionIndx >= len(directions)):
        curDirectionIndx = 0

    curNode = nextNode

    step += 1


print(step)

#res = puzzleFirstHalf(inp)
#res1 = puzzleSecondHalf(inp)

#print("Part 1 result: " + str(res))
#print("Part 2 result: " + str(res1))'''
