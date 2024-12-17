import re

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def checkNext(data, char, loc):
    x,y = loc
    if char == 'M':
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(data) and 0 <= ny < len(data[0]):
                if data[nx][ny] == char:
                    if checkNext(data, 'A', (nx, ny)) != None:
                        
    elif char == 'A':
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(data) and 0 <= ny < len(data[0]):
                if data[nx][ny] == char:
                    if checkNext(data, 'S', (nx, ny)) != None:
                        
    elif char == 'S':
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(data) and 0 <= ny < len(data[0]):
                if data[nx][ny] == char:
                    True
                        
    return True

def half_1(inp):
    sum = 0
    data = [list(line.strip()) for line in inp]
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'X':
                if checkNext(data, 'M', (i, j)) != None:
                    print("XM", checkNext(data, 'M', (i, j)))

    return sum

def half_2(inp):
    return


inpFile = open("input.txt", "r")
inp = inpFile.readlines()

print("Answer to Part 1:", half_1(inp))
print()
#print("Answer to Part 2:", half_2(inp))


















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
