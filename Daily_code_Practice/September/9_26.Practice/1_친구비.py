from dataclasses import field
import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n, m, k = map(int, input().split())
money = [0] + list(map(int, input().split()))


matrix = [[] for _ in range(n+1)]
check = [False] * (n+1)
friend = []

for _ in range(m):
    y, x = map(int, input().split())

    matrix[y].append(x)
    matrix[x].append(y)

def dfs(y, arr):
    for j in matrix[y]:
        if not check[j]:
            check[j] = True
            arr.append(j)
            dfs(j,arr)

for i in range(1,n+1):
    if not check[i]:
        check[i] = True
        arr = [i]
        dfs(i, arr)
        friend.append(arr)

result = 0

for fri in friend:
    cost = sys.maxsize
    for j in fri:
        if cost > money[j]:
            cost = money[j]
    result += cost

if result <= k:
    print(result)
else:
    print('Oh no')

