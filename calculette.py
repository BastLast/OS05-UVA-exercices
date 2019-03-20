import sys

lines = sys.stdin.readlines()
nb = []
for line in lines :
    line = line.rstrip()
    lineTab = line.split(" ")
    resultat = -1
    erreur = 0
    for i in lineTab :
        if i == '*' or i == '+' :
            if len(nb) < 1 :
                erreur = 1
            if erreur == 0 :
                if resultat == -1 :
                    if len(nb) == 1:
                        erreur = 1
                    else :
                        nb1 = nb.pop()
                else:
                    nb1 = resultat
                nb2 = nb.pop()
                if i == '*':
                    resultat = nb1 * nb2
                else :
                    resultat = nb1 + nb2
        else :
            nb.append(int(i))
    if erreur == 1:
        print("Expression invalide")
    else :
        if(len(nb)== 1) :
            print(nb.pop()) 
        else:
            if(len(nb)== 0) :
                print(resultat)
            else:
                print("Expression invalide")