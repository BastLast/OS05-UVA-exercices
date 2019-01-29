import sys

lines = sys.stdin.readlines()
dictionary = {}
count = 0
for line in lines:
    lineTab = list(map(str, line.split()))
    if count == 1:
        if lineTab[0] in dictionary:
            print(dictionary.get(lineTab[0]))
        else:
            print('eh')
    if not lineTab:
        count = 1
    if count == 0:
        dictionary[lineTab[1]] = lineTab[0]

