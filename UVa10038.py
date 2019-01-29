import sys

lines = sys.stdin.readlines()

valeurs = {}
for line in lines:
    count = 0
    lineTab = list(map(int, line.split()))
    if len(lineTab) == lineTab[0]+1:
        for i in range(1, lineTab[0]):
            valeurs[abs(lineTab[i]-lineTab[i+1])] = 1

        for i in range(1, lineTab[0]):
            if i in valeurs:
                del valeurs[i]
            else:
                count = 1

        if count == 1:
            print('Not jolly')
        else:
            print('Jolly')
