def half_1(inp):
    leftList = []
    rightList = []

    for line in inp:
        line = line.strip().split()
        leftList.append(int(line[0]))
        rightList.append(int(line[1]))
    leftList.sort()
    rightList.sort()

    sums = []

    for i in range(len(leftList)):
        sums.append(abs(leftList[i] - rightList[i]))
    return sum(sums)

def half_2(inp):
    leftList = []
    rightList = []

    for line in inp:
        line = line.strip().split()
        leftList.append(int(line[0]))
        rightList.append(int(line[1]))
    sum = 0
    for id in leftList:
        sum = sum + rightList.count(id) * id
    return sum



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
