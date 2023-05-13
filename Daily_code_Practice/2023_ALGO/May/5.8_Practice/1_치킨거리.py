import sys
sys.stdin = open("1_input.txt", "r")
from itertools import combinations
input = sys.stdin.readline

n, m = map(int,input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
chicken_shop = []
house = []

for j in range(n):
    for i in range(n):
        if matrix[j][i] == 2:
            chicken_shop.append((j,i))
        if matrix[j][i] == 1:
            house.append((j,i))

result = sys.maxsize

for p_chicken_shop in combinations(chicken_shop, m):
    
    result_sum = 0
    for y, x in house:
        chicken_load = sys.maxsize
        for chicken in p_chicken_shop:
            load_sum = abs(y-chicken[0]) + abs(x-chicken[1])
            chicken_load = min(chicken_load, load_sum)
        
        result_sum += chicken_load
    
    result = min(result, result_sum)
print(result)

        
        





