import sys


sys.path.append('C:/Users/samu.tiainen/Documents/Personal/AdventOfCode/aoc2022')
from utils import getLines

# input = getLines(open("./d2/test.txt", "r"), True, " ")
input = getLines(open("./d2/input.txt", "r"), True, " ")

def getResultPoints(strategy):
    atk = strategy[0]
    res = strategy[1]
    match atk:
        case "A":
            if res == "X":
                return 3
            if res == "Y":
                return 6
            if res == "Z":
                return 0
        case "B":
            if res == "X":
                return 0
            if res == "Y":
                return 3
            if res == "Z":
                return 6
        case "C":
            if res == "X":
                return 6
            if res == "Y":
                return 0
            if res == "Z":
                return 3
    return 0

def getShapePoints(strategy):
    match strategy[1]:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3
    return 0

result = 0
for strategy in input:
    result += getResultPoints(strategy)
    result += getShapePoints(strategy)

print(result)

