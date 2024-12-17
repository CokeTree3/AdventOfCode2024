with open('input.txt', 'r') as file:
    inp = file.read().split("\n\n")

rules = inp[0].strip().splitlines()
rules = [tuple(map(int, line.split('|'))) for line in rules]
updates = [list(map(int, line.split(','))) for line in inp[1].strip().splitlines()]

wrongLists = []

def checkRules(first, second):
    for rule in rules:
        if (first, second) == rule:
            return True
    return False

def half_1():
    sum = 0
    for line in updates:
        correct = True
        for i in range(len(line)-1, 0, -1):
            for j in range(i - 1, -1, -1):
                if(checkRules(line[i], line[j])):
                    correct = False
                    break
            if not correct:
                break
        if correct:
            sum += line[len(line) // 2]
        else:
            wrongLists.append(line)

    return sum

def half_2():
    sum = 0
    for line in wrongLists:
        for i in range(len(line)-1, 0, -1):
            for j in range(i - 1, -1, -1):
                if(checkRules(line[i], line[j])):
                    temp = line[j]
                    line[j] = line[i]
                    line[i] = temp
                    j = i - 1
        sum += line[len(line) // 2]
            
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
