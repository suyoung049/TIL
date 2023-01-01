import sys
sys.stdin = open('5_input.txt', 'r')
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = list(list(map(int, input().split())) for _ in range(n))

result = sys.maxsize
chick = []
home = []

for j in range(n):
    for i in range(n):
        if matrix[j][i] == 1:
            home.append((j,i))
        
        if matrix[j][i] == 2:
            chick.append((j,i))


for chi in combinations(chick, m):
    temp = 0
    for ho in home:
        chi_len = sys.maxsize
        for j in range(m):
            chi_len = min(chi_len, abs(ho[0]-chi[j][0]) + abs(ho[1]-chi[j][1]))
        temp += chi_len
    
    result = min(result, temp)

print(result)