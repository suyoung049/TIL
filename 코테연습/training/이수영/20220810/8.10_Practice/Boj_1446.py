import sys

sys.stdin = open("14467_input.txt", "r")
N = int(input())

cow = {}
coun = 0


for i in range(N):
    k, v = map(int, input().split())
    if k in cow and cow[k] != v:
        coun += 1
    cow[k] = v
print(coun) 
    
