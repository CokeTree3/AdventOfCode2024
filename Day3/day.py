import re

def half_1(inp):
    sum = 0
    for line in inp:
        line = line.strip()
        instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
        for ins in instructions:
            data = re.match(r"mul\((\d+),(\d+)\)", ins)
            res = int(data.group(1)) * int(data.group(2))
            sum += res
    return sum

def half_2(inp):
    sum = 0
    enabled = True
    for line in inp:
        line = line.strip()
        instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
        remainder = re.split(r"mul\(\d{1,3},\d{1,3}\)", line)

        for i in range(len(instructions)):
            cond = re.findall(r"do\(\)|don't\(\)", remainder[i])
            if cond:
                enabled = cond[-1] == "do()"
            
            if enabled:
                data = re.match(r"mul\((\d+),(\d+)\)", instructions[i])
                res = int(data.group(1)) * int(data.group(2))
                sum += res
    return sum


inpFile = open("input.txt", "r")
inp = inpFile.readlines()

print("Answer to Part 1:", half_1(inp))
print()
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
