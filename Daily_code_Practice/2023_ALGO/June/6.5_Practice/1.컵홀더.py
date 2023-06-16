import sys
sys.stdin = open("1_input.txt","r")

n = int(input())

for _ in range(n):
    text = input()
    result = ""
    for chr in text:
        chr = chr.lower()
        result += chr
    print(result)
    


