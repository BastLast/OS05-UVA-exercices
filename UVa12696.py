import sys

lines = sys.stdin.readlines()
count = 0
for line in lines:
    lineTab = list(map(float, line.split()))
    if len(lineTab) == 4:
        result = 1
        if lineTab[0] > 56.00:
            result = 0

        if lineTab[1] > 45.00:
            result = 0

        if lineTab[2] > 25.00:
            result = 0

        if (lineTab[0]+lineTab[1]+lineTab[2]) <= 125.00:
            result = 1

        if lineTab[3] > 7.00:
            result = 0

        if result == 1:
            count = count+1

        print(result)
print(count)
