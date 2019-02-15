import sys

lines = sys.stdin.readlines()
del lines[0]
banque = {}
banque[']'] = '['
banque[')'] = '('

for line in lines:
    lineTab = ' '.join(line).split()
    piledeverif = []
    
    for i in range(0, len(lineTab)):
        if not piledeverif:
            dernierElement = ''
        else:
            dernierElement = piledeverif.pop()
            
        if lineTab[i] == '[' or lineTab[i] == '(' :
            if dernierElement != '' :
                piledeverif.append(dernierElement)
            piledeverif.append(lineTab[i])   
        else:
            if banque[lineTab[i]] != dernierElement:
                piledeverif.append("r")
                piledeverif.append("r")
                
    if piledeverif != []:
        print('No')
    else:
        print('Yes')
