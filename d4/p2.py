input = [i.strip().split(",") for i in open("input.txt", "r").readlines()]

def doesContain(x, y):
    return y[0] <= x[1] and y[1] >= x[0]

count = 0
for pair in input:
    firstRange = [int(i) for i in pair[0].split("-")]
    secondRange = [int(i) for i in pair[1].split("-")]
    if doesContain(firstRange, secondRange):
        count += 1

print(count)