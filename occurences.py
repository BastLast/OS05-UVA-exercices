import sys
lines = sys.stdin.readlines()
dico = {}
for line in lines :
    lineTab = line.split(" ")
    count = 0
    for element in lineTab :
        element = element.lower()
        element = element.rstrip('.')
        element = element.rstrip(',')
        count = count +1

        if element in dico :
            nb = dico[element]
            dico[element] = nb+1
        else :
            dico[element] = 1

maxim = 0
for mots in dico :
    if dico[mots] > maxim :
        maxim = dico[mots]
resultat = str(maxim)
motsaff =[]
for mots in dico :
    if dico[mots] == maxim :
        motsaff.append(mots)
motsaff.sort()
for mots in motsaff :
    resultat = resultat+ " " + mots
print(resultat)