import sys


sys.path.append('C:/Users/samu.tiainen/Documents/Personal/AdventOfCode/aoc2022')
from utils import getLines


# input = open("./d1/input.txt", "r")
input = open("./d1/test.txt", "r")

res = getLines(input)
print(res)

elfs = []
elf = []
for line in input.readlines():
    if line == "\n":
        elfs.append(sum(elf))
        elf = []
    else:
        elf.append(int(line))

elfs.sort(reverse=True)
top3 = elfs[:3]
print(sum(top3))