def getLines(file, useStrings: bool = False, split = None):
    inputList = []
    lines = file.readlines()
    if len(lines) == 1 and split != None:
        inputList = int(line.split(split))
    else:
        for line in lines:
            if(line == "\n"):
                inputList.append(None)
            elif useStrings:
                if split == None:
                    inputList.append(line)
                else:
                    inputList.append(line.rstrip().split(split))
            else:
                if split == None:
                    inputList.append(int(line))
                else:
                    inputList.append([eval(i) for i in line.split(split)])
    return inputList
                    

