import sys

lines = sys.stdin.readlines()
count = 0
numbers = {}
origin = {}
todisplay = []
for line in lines:
    lineTab = list(map(str, line.split()))
    if lineTab[0] == "Register" :
        numbers[lineTab[1]] = int(lineTab[2])
        origin[lineTab[1]] = int(lineTab[2])
    if count == 1 :
        iterations = int(lineTab[0])
        while iterations>0 :
            for key,value in numbers.items() :
                numbers[key] = value -1
                if numbers[key] == 0:
                    if iterations > 0 :
                        todisplay.append(key)
                        iterations = iterations -1 
                        numbers[key] = origin[key]
            todisplay.sort()
            for element in todisplay :
                print(element)
            todisplay = []
    if "#" in lineTab[0] :
        count = 1