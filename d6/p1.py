input = open("input.txt", "r").read()

four = []
fail = True
for i in range(0, len(input)-4):
    four = input[i:i+4]
    c1 = four.count(four[0]) == 1
    c2 = four.count(four[1]) == 1
    c3 = four.count(four[2]) == 1
    c4 = four.count(four[3]) == 1

    if c1 and c2 and c3 and c4:
        print(i+4)
        break

