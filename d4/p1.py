input = [i.strip().split(",") for i in open("input.txt", "r").readlines()]

def doesContain(x, y):
    return x[0] <= y[0] and x[1] >= y[1]


count = 0
for pair in input:
    firstRange = [int(i) for i in pair[0].split("-")]
    secondRange = [int(i) for i in pair[1].split("-")]
    if doesContain(firstRange, secondRange) or doesContain(secondRange, firstRange):
        count += 1

print(count)