import json


inputLines = open("./d7/input.txt", "r").readlines()

filesystem = {"/": {}}

def printDict(dict):
    print(json.dumps(dict, indent=2))

def findParent(child, node):
    for key in node:
        if "size" in node[key].keys(): 
            continue
        if child in node[key].keys():
            return key
        res = findParent(child, node[key])
        if res != None:
            return res

def addObjectToTree(currentDir, objectToAdd, node):
    if currentDir in node.keys():
        node[currentDir].update(objectToAdd)
        return node
    else:
        for key in node:
            if "size" not in node[key].keys():
                res = addObjectToTree(currentDir, objectToAdd, node[key])
                node[key] = res
    return node

def calculateTotals(node):
    curTotal = 0
    for key in node:
        if key == "totalSize":
            continue
        if "size" in node[key].keys():
            curTotal += node[key]["size"]
            continue
        else:
            node[key].update(calculateTotals(node[key]))
            curTotal += node[key]["totalSize"]
    
    node.update({"totalSize": curTotal})
    return node
            

currentDir = ""
for line in inputLines:
    parts = line.strip().split(" ")
    if parts[0] == "$":
        if parts[1] == "cd":
            if parts[2] == "..":
                currentDir = findParent(currentDir, filesystem)
            else:
                currentDir = parts[2]
    if parts[0] == "dir":
        filesystem = addObjectToTree(currentDir, {parts[1]: {}}, filesystem)
    if parts[0].isnumeric():
        filesystem = addObjectToTree(currentDir, {parts[1]: {"size": int(parts[0])}}, filesystem)

# printDict(filesystem)
# def findDoubleDirs(node):
#     for key in node:
#         if key == "totalSize":
#             continue
#         if "size" in node[key].keys():
#             continue
#         else:
#             if list(node.keys()).count(key) > 1:
#                 print("Double:", key)
#             findDoubleDirs(node[key])
# findDoubleDirs(filesystem)

filesystem = calculateTotals(filesystem)

def getTotalSizeOfBigDirs(node):
    total = 0
    for key in node:
        if key == "totalSize" or "size" in node[key].keys():
            continue
        if "totalSize" in node[key]:
            if node[key]["totalSize"] <= 100000:
                total += node[key]["totalSize"]
        total += getTotalSizeOfBigDirs(node[key])
    return total

print(getTotalSizeOfBigDirs(filesystem))