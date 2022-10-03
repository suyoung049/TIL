import sys
sys.stdin = open('4_input.txt', 'r')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


T = int(input())

for _ in range(T):

    n, m = map(int, input().split())

    matrix = [[] for _ in range(n+1)]

    check = [0] * (n+1)

    result = True


    for _ in range(m):
        y, x = map(int, input().split())

        matrix[y].append(x)
        matrix[x].append(y)

    def dfs(i, n):
        global result

        if not result:
            return
        
        check[i] = n
        
        for j in matrix[i]:
            if not check[j]:
                dfs(j,-n)

            elif check[i] == check[j]:
                result = False
                return
        



    for i in range(1, n+1):
        if not check[i]:
            dfs(i, 1)

            if not result:
                break

    print(result)

