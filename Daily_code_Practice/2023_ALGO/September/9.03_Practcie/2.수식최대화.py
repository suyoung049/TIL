from itertools import combinations
expression = "100-200*300-500+20"

lis = []
formula = []
num = ""
for chr in expression:
    if chr.isdigit():
        num += chr
    else:
        lis.append(num)
        num = ""
        lis.append(chr)
        formula.append(chr)

