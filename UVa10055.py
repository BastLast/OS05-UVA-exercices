import sys

lines = sys.stdin.readlines()

if lines[-1] == '':

    for line in lines:
        lineTab = list(map(int,line.split()))
        if lineTab[0]>lineTab[1] :
            print(lineTab[0]-lineTab[1])
        else:
            print(lineTab[1]-lineTab[0])