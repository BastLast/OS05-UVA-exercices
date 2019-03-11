import sys
lines = sys.stdin.readlines()
count = 0
taille = 0
for line in lines :
    liste = []
    lineTab = list(map(float,line.split()))
    if count == 1:
        i=1
        while i <= int(lineTab[0]) :
            liste.append(lineTab[i])
            i = i+1
    if count == 0:
        taille = lineTab[0]
        count = 1

    liste.sort()
    if lineTab[0] == 0 :
            print("Vide")
    else :
        if len(liste) != 0 :
            if len(liste)%2 ==0 :
                resultat = (liste[int(len(liste)/2)-1] + liste[int(len(liste)/2)] ) /2
            else :
                resultat =liste[int(len(liste)/2)] 

            print('{x:.2f}'.format(x=resultat))       