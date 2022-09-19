import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n, m , k = map(int, input().split())

matrix = [[] for _ in range(n+1)]
visit = [0] * (n+1)
count = 1

for _ in range(m):
    x, y = map(int, input().split())

    matrix[x].append(y)
    matrix[y].append(x)

for i in range(len(matrix)):
    matrix[i].sort()
print(matrix)

def dfs(start):
    global count 
    visit[start] = count

    for i in matrix[start]:
        if visit[i] == 0:
            count += 1
            dfs(i)

dfs(k)

for i in range(1,n+1):
    print(visit[i], end = ' ')