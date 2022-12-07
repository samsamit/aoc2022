import json


inputLines = open("./d7/test.txt", "r").readlines()

filesystem = {"/": {}}



def findParent(child, node):
    for key in node:
        if key == "file": 
            continue
        if child in node[key].keys():
            return key
        res = findParent(child, node[key])
        if res != None:
            return res

def addObjectToTree(currentDir, objectToAdd, node):
    print(node.keys())
    if currentDir in node.keys():
        node[currentDir].update(objectToAdd)
        return node
    else:
        for key in node:
            if key != "file":
                res = addObjectToTree(currentDir, objectToAdd, node[key])
                node[key] = res
    return node

currentDir = ""
for line in inputLines:
    parts = line.strip().split(" ")
    if parts[0] == "$":
        if parts[1] == "cd":
            if parts[2] == "..":
                currentDir = findParent(currentDir, filesystem)
                continue
            else:
                currentDir = parts[2]
        if parts[1] == "ls":
            continue
    if parts[0] == "dir":
        filesystem = addObjectToTree(currentDir, {parts[1]: {}}, filesystem)
        continue
    if parts[0].isnumeric():
        print("numeric", parts[0], parts[1])
        filesystem = addObjectToTree(currentDir, {"file": {"name": parts[1],"size": int(parts[0])}}, filesystem)
        continue

print(json.dumps(filesystem, indent=2))