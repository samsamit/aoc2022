import string


input = [i.strip() for i in open("input.txt", "r").readlines()]

groups = []
pos = 0
while pos < len(input):
    chunk = input[pos:pos+3]
    groups.append(chunk)
    pos += 3

values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = 26 + index + 1

commons = []
done = False
for group in groups:
    for char in group[0]:
        if char in group[1] and char in group[2]:
            commons.append(char)
            done = True
            break
    if done: continue
    for char in group[1]:
        if char in group[0] and char in group[2]:
            commons.append(char)
            done = True
            break
    if done: continue
    for char in group[2]:
        if char in group[0] and char in group[1]:
            commons.append(char)
            break

total = 0
for common in commons:
    total += values[common]

print(total)