import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    matrix = [[] for _ in range(n+1)]
    check = [False] * (n+1)
    error = False

    for _ in range(m):
        y, x = map(int, input().split())

        matrix[y].append(x)
        matrix[x].append(y)
    
    print(matrix)
    
    def dfs(y, n):
        global error

        if error:
            return

        check[y] = n

        for i in matrix[y]:
            if not check[i]:
                dfs(i, -n)

            if check[y] == check[i]:
                error = True
                return

    for i in range(1, n+1):
        if not check[i]:
            dfs(i, 12)

            if error:
                break
    
    print(error)

    