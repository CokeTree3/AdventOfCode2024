inpFile = open("input.txt", "r")
inp = list(inpFile.readline().strip())
list = [int(char) for char in inp]

print(inp)

def findNextFree(start, list):
    for i in range(start, len(list)):
        if(list[i] == '.'):
            return i
    return -1

def half_1():
    sum = 0
    id = 0
    processed = []
    freeSpot = list[0]
    for i, elem in enumerate(list):
        if i % 2 == 0:
            processed.extend([id] * elem)
            id += 1
        else:
            processed.extend(elem * ['.'])

    for elem in range(len(processed) -1, -1, -1):
        processed[freeSpot] = processed[elem]
        freeSpot = findNextFree(freeSpot, processed)
        processed[elem] = '-'
        if(freeSpot == -1):
            break
    for i in range(len(processed)):
        if processed[i] == '-':
            break
        sum += i * processed[i]
    return sum

def half_2():
    sum = 0
    id = 0
    processed = []
    freeSpot = list[0]
    for i, elem in enumerate(list):
        if i % 2 == 0:
            processed.extend([id] * elem)
            id += 1
        else:
            processed.extend(elem * ['.'])

    for elem in range(len(processed) -1, -1, -1):
        processed[freeSpot] = processed[elem]
        freeSpot = findNextFree(freeSpot, processed)
        processed[elem] = '-'
        if(freeSpot == -1):
            break
    for i in range(len(processed)):
        if processed[i] == '-':
            break
        sum += i * processed[i]
    return sum

print("Answer to Part 1:", half_1())
print()
print("Answer to Part 2:", half_2())
















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
