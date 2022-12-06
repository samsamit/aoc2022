input = open("input.txt", "r").read()
print([len(input[i:i+14]) == len(set(input[i:i+14])) for i in range(0, len(input)-14)].index(True) + 14)