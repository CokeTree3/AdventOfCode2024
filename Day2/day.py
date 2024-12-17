def half_1(inp):
    safe = 0

    for line in inp:
        line = line.strip().split()
        line = list(map(int, line))
        ord = True
        if line[0] - line[1] > 0:
            ord = False
        else:
            ord = True
        good = True
        for i in range(len(line) - 1):
            if line[i] == line[i + 1] or abs(line[i] - line[i + 1]) > 3:
                good = False
                break
            if (line[i] > line[i+1] and ord) or (line[i] < line[i+1] and not ord):
                good = False
                break
                
        if good:
            print(line)
            safe += 1
    
    return safe

def half_2(inp):
    safe = 0

    for line in inp:
        line = line.strip().split()
        line = list(map(int, line))

        ord = True
        ordVal = 0
        for i in range(len(line) - 1):
            if line[i] - line[i+1] > 0:
                ordVal -= 1
            elif line[i] - line[i+1] < 0:
                ordVal += 1
        if ordVal < 0:
            ord = False
        elif ordVal == 0:
            print( "is 0")
            print(line)
            continue

        good = True
        removeUsed = False
        for i in range(len(line) - 1):
            if line[i] == line[i + 1] or abs(line[i] - line[i + 1]) > 3 or (line[i] > line[i+1] and ord) or (line[i] < line[i+1] and not ord):
                if removeUsed:
                    good = False
                    break
                if i < len(line) - 2 and (line[i] == line[i + 2] or abs(line[i] - line[i + 2]) > 3 or (line[i] > line[i+2] and ord) or (line[i] < line[i+2] and not ord)):
                    if i == 0 and (line[i+1] != line[i + 2] and abs(line[i+1] - line[i + 2]) <= 3):
                        if not ((line[i+1] > line[i+2] and ord) or (line[i+1] < line[i+2] and not ord)):
                            removeUsed = True
                            continue
                    good = False
                    break
                removeUsed = True
                
        if good:

            safe += 1
    
    return safe


inpFile = open("input.txt", "r")
inp = inpFile.readlines()


print("Answer to Part 1:", half_1(inp))
print("Answer to Part 2:", half_2(inp))


















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
