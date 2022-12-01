input = open("./input.txt", "r")
# input = open("./test.txt", "r")

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