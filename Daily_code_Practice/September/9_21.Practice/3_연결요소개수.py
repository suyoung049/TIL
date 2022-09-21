import sys
sys.stdin = open('3_input.txt', 'r')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [[] for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(m):
    y, x = map(int, input().split())

    matrix[y].append(x)
    matrix[x].append(y)

def dfs(y):
    check[y] = True

    for i in matrix[y]:
        if check[i] == False:
            check[i] = True
            dfs(i)

count = 0
for j in range(1, n+1):
    if check[j] == False:
        dfs(j)
        count += 1

print(check)
print(count)
