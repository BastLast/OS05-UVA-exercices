import sys

lines = sys.stdin.readlines()
count = 0
resultat = 0
panier = {}
for line in lines :
    line = line.rstrip('\n')
    lineTab = line.split(" ")
    if count == 1:
        if lineTab[1] in panier :
            resultat = float(resultat) + float(lineTab[0]) * float(panier[lineTab[1]])
        else :
            count = 3
    if lineTab[0] == "":
        count = 1
    if count == 0:
        panier[lineTab[0]] = lineTab[1]
if count == 3 :
    print('Panier invalide')
else :
    print('{x:.2f}'.format(x=resultat))