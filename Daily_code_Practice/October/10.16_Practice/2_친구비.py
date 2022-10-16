import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n, m, k = map(int, input().split())

money = [0] + list(map(int, input().split()))

matrix = [[] for _ in range(n+1)]
check = [False]*(n+1)
friends = []


for _ in range(m):
    y, x = map(int, input().split())
    matrix[y].append(x)
    matrix[x].append(y)


def dfs(y, arr):
    for i in matrix[y]:
        if not check[i]:
            check[i] =  True
            arr.append(i)
            dfs(i, arr)



for i in range(1, n+1):
    if not check[i]:
        arr = [i]
        check[i] = True
        dfs(i, arr)
        friends.append(arr)

result = 0

for friend in friends:
    inf = sys.maxsize
    for i in friend:
        if inf > money[i]:
            inf = money[i]
    result += inf

if result <= k:
    print(result)

else:
    print('oh no')

        

