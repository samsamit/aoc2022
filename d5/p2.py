input = open("input.txt", "r").read()
packetSize = 14
four = []
fail = True
for i in range(0, len(input)-packetSize):
    packet = input[i:i+packetSize]
    success = []
    for char in packet:
        success.append(packet.count(char) == 1)

    if all(success):
        print(i+packetSize)
        break

