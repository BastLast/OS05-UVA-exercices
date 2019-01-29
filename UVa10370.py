import sys

lines = sys.stdin.readlines()
count = 0
for line in lines:
    lineTab = list(map(int, line.split()))
    if len(lineTab) == lineTab[0]+1:
        somme = 0
        for i in range(1, lineTab[0]+1):
            somme = somme + lineTab[i]
        moyenne = (somme / lineTab[0])

        nb = 0
        for i in range(1, lineTab[0]+1):
            if lineTab[i] > moyenne:
                nb = nb + 1
        result = round((nb/lineTab[0])*100, 3)
        print('{x:2.3f}%'.format(x=result))
