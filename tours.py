import sys
lines = sys.stdin.readlines()
count = 0
taille = 0
colonnes = set()
lignes = set()
for line in lines :
    lineTab = list(map(int,line.split()))
    if count == 1:
        colonnes.add(lineTab[0])
        lignes.add(lineTab[1])
    if count == 0:
        taille = lineTab[0]
        count = 1
erreur = 0
x=0
y=0

if len(colonnes) == taille or len(lignes) == taille :
    print("Emprise totale")
else : 
    for i in range(1,taille+1) :
        if erreur ==1 :
            break
        if i not in colonnes :
           for k in range(1,taille+1) :
               if k not in lignes :
                   if erreur ==0 :
                        x = i
                        y = k
                        erreur = 1
                        break
                        

    if erreur == 1 :
        print(x , y)
    else :
        print("Emprise totale")