import json


inputLines = open("./d7/test.txt", "r").readlines()
class DirNode:
    def __init__(self, name) -> None:
        self.name = name
        self.childs = []
        pass

    def addChild(self, path, child):
        print(path)
        path.pop(0)
        if len(path) == 0:
            self.childs.append(child)
        else:
            for child in self.childs:
                if child.__class__.__name__ == "DirNode" and child.name == path[0]:
                    child.addChild(path.copy(), child)

    def print(self):
        for child in self.childs:
            if child.__class__.__name__ == "DirNode":
                print("Dir:", child.name)
                child.print()
            else:
                print("File:", child.name, child.size)

class FileNode:
    def __init__(self, size, name) -> None:
        self.size = size
        self.name = name
        pass

class FileTree:
    def __init__(self) -> None:
        self.tree = DirNode("/")
        pass

    def addDir(self, path, dirName):
        # print(path)
        self.tree.addChild(path.copy(), DirNode(dirName))
        
    def addFile(self, path, name, size):
        self.tree.addChild(path.copy(), FileNode(size, name))

    def print(self):
        print(self.tree.childs)
        self.tree.print()

fileTree = FileTree()
breadcrumbs = []
for line in inputLines:
    command = line.strip().split()
    if command[0] == "$":
        match command[1]:
            case "cd":
                match command[2]:
                    case "..":
                        breadcrumbs.pop()
                    case _:
                        breadcrumbs.append(command[2])
            case "ls":
                continue
    if command[0].isnumeric():
        fileTree.addFile(breadcrumbs.copy(), command[1], command[0])
    if command[0] == "dir":
        fileTree.addDir(breadcrumbs.copy(), command[1])
    print(breadcrumbs)

fileTree.print()