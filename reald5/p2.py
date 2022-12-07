inputLines = open("./d5/input.txt", "r").readlines()

takingCraneYeard = True
yard = []
instructions = []
for line in inputLines:
    if line == "\n":
        takingCraneYeard = False
        continue

    if takingCraneYeard:
        row = []
        for i in range(1, len(line)-2):
            if i % 2 or i == 1:
                row.append(line[i])
        del row[1::2]
        yard.append(row)
    else:
        instruction = line.strip().split(" ")
        instructions.append(instruction)
yard.pop()

stacks = []
for i in range(0, len(yard[0])):
    stack = []
    for row in yard:
        if row[i] != " ":
            stack.append(row[i])
    stacks.append(stack)

def makeAMove(moveArr, stacks):
    count = int(moveArr[1])
    where = int(moveArr[3])
    to = int(moveArr[5])

    newStacks = [*stacks]

    crates = newStacks[where-1][:count]
    del newStacks[where-1][:count]
    newStacks[to-1] = crates + newStacks[to-1]

    return newStacks

for instruction in instructions:
    stacks = makeAMove(instruction, stacks)

letters = ""
for stack in stacks:
  letters += stack[0]

print(letters)