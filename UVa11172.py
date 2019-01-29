import sys

lines = sys.stdin.readlines()

for line in lines:
    lineTab = list(map(int, line.split()))
    if len(lineTab) == 2:
        print({True: "=",
               lineTab[1] < lineTab[0]: ">",
               lineTab[1] > lineTab[0]: "<"
               }[True])
