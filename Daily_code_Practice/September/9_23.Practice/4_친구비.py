import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n, m, k = map(int, input().split())

money = [0] + list(map(int, input().split()))

matrix = [[] for _ in range(n+1)]
check = [False] * (n+1)
friends =[]

for _  in range(m):
    y, x = map(int, input().split())

    matrix[y].append(x)
    matrix[x].append(y)

def dfs(y, arr):                # 연결 노드들 정리 위한 함수 지정
    for i in matrix[y]:
        if not check[i]:
            check[i] = True
            arr.append(i)
            dfs(i,arr)

for i in range(1, n+1):
    if not check[i]:
        arr = [i]
        check[i] = True
        dfs(i, arr)
        friends.append(arr)


result = 0

for friend in friends:
    cost = sys.maxsize
    for j in friend:
        if cost > money[j]:
            cost = money[j]
    result += cost

if result <= k:
    print(result)

else:
    print('Oh no')

