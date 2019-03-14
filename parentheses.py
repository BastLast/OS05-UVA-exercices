import sys

lines = sys.stdin.readlines()
del lines[0]

for line in lines:
    lineTab = ' '.join(line).split()
    count = 0
    erreur = 0
    for i in range(0, len(lineTab)):
        if lineTab[i] == '(' :
           count = count +1
        if lineTab[i] == ')' :
           count = count -1
           if count < 0 :
               erreur = 1
                      
    if count != 0:
        print('False')
    else:
        if erreur == 1 :
            print('False')
        else:
            print('True')
