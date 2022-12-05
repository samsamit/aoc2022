import string


input = [i.strip() for i in open("input.txt", "r").readlines()]

rucksacks = []
for line in input:
    size = int(len(line) / 2)
    rucksacks.append([line[:size], line[size:]])

values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = 26 + index + 1


commons = []
found = False
for sack in rucksacks:
    for char in sack[0]:
        if char in sack[1]:
             commons.append(char)
             found = True
             break
    if found:
        found = False
        continue

total = 0
for common in commons:
    total += values[common]

print(total)