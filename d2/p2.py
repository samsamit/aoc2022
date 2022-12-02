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
                return 0 + getShapePoints("Z")
            if res == "Y":
                return 3 + getShapePoints("X")
            if res == "Z":
                return 6 + getShapePoints("Y")
        case "B":
            if res == "X":
                return 0 + getShapePoints("X")
            if res == "Y":
                return 3 + getShapePoints("Y")
            if res == "Z":
                return 6 + getShapePoints("Z")
                return 6
        case "C":
            if res == "X":
                return 0 + getShapePoints("Y")
            if res == "Y":
                return 3 + getShapePoints("Z")
            if res == "Z":
                return 6 + getShapePoints("X")
    return 0

def getShapePoints(letter):
    match letter:
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

print(result)

