import sys
from itertools import combinations
sys.stdin = open('2_input.txt')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = sys.maxsize

chick = []
house = []

for j in range(n):
    for i in range(n):
        if matrix[j][i] == 1:
            house.append((j,i))
        
        if matrix[j][i] == 2:
            chick.append((j,i))

print(chick)

for choice_chick in combinations(chick, m):
    temp = 0
    for h in house:
        chi_len = sys.maxsize
        for j in range(m):
            chi_len = min(chi_len, abs(h[0]-choice_chick[j][0]) + abs(h[1] - choice_chick[j][1]))
        temp += chi_len
    
    result = min(result, temp)

print(temp)