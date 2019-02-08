import sys
# CETTE SOLUTION NE FONCTIONNE PAS PARFAITEMENT. Il serait préférable d'utiliser heap
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

# Solution à privilegier
import sys
from _heapq import heappush, heappop
lines = sys.stdin.readlines()
if lines[-1] == '':
    del lines[-1]
h = []
rep = 0
for line in lines:
    tableau = line.split()
    if len(tableau) == 3:
        heappush(h, (int(tableau[2]), int(tableau[1]), int(tableau[2])))
    if len(tableau) == 1 and tableau[0] != "#":
        rep = int(tableau[0])
while rep > 0:
     temp = heappop(h)
     print(temp[1])
     heappush(h, (int(temp[0]+temp[2]), int(temp[1]), int(temp[2])))
     rep = rep - 1