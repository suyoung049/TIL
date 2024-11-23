import sys
from copy import deepcopy
sys.setrecursionlimit(10**7)
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

comb_list = []
def comb(chicken, candidate, m, i):
    length = len(chicken)
    global comb_list
    if len(candidate) == m:
        copy = deepcopy(candidate)
        comb_list.append(copy)
        return
    
    
    for k in range(i, length):
        candidate.append(chicken[k])
        comb(chicken, candidate, m, k + 1)
        candidate.pop()
           
    
def pprint(matrix):
    for x in matrix:
        print(x)

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

chicken = []
house = []
candidate = []
for j in range(n):
    for i in range(n):
        if matrix[j][i] == 2:
            chicken.append((j,i))
        elif matrix[j][i] == 1:
            house.append((j,i))

comb(chicken, candidate, m, 0)
INF = float('inf')

min_total_root = INF
for comb in comb_list:
    total_root = 0
    for home in house:
        min_root = INF
        for chicken_shop in comb:
            root = abs(home[0] - chicken_shop[0]) + abs(home[1] - chicken_shop[1])
            min_root = min(min_root, root)
        total_root += min_root
    min_total_root = min(min_total_root, total_root)

print(min_total_root)

        
            

    









