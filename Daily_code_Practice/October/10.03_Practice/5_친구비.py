import sys
sys.stdin = open('5_input.txt', 'r')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, k = map(int, input().split())
money = [0] + list(map(int, input().split()))
friend = []

matrix = [[] for _ in range(n+1)]

check = [False] * (n+1)

for _ in range(m):
    y, x = map(int, input().split())

    matrix[y].append(x)
    matrix[x].append(y)

def dfs(i, arr):
    for j in matrix[i]:
        if not check[j]:
            check[j] = True
            arr.append(j)
            dfs(j, arr)


for i in range(1, n+1):
    if not check[i]:
        check[i] = True
        arr = [i]
        dfs(i, arr)
        friend.append(arr)

print(friend)

result = 0

for i in friend:
    inf = sys.maxsize
    for j in i:
        if money[j] < inf:
            inf = money[j]
        
    result += inf

if result <= k:
    print(result)

else:
    print('OH NO')


    

