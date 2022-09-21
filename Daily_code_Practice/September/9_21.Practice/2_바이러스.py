import sys
sys.stdin = open('2_input.txt', 'r')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
m = int(input())

matrix = [[] for _ in range(n+1)]
check = [False] * (n+1)
result = []

for _ in range(m):
    y, x = map(int, input().split())

    matrix[y].append(x)
    matrix[x].append(y)


def dfs(y):
    check[y] = True
    result.append(y)

    for i in matrix[y]:
        if check[i] == False:
            check[i] = True
            dfs(i)

dfs(1)

print(len(result)-1)