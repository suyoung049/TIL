import sys
sys.stdin = open('6_input.txt','r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(n)]
    count = 0

    for y in range(m):
        for x in range(n-1, -1, -1):

            if matrix[x][y] == 1:

                while True:

                    if x+1 >= n:
                        break
                    if matrix[x+1][y] == 1:
                        break

                    matrix[x][y] = 0
                    matrix[x+1][y] = 1

                    x += 1
                    count += 1

    print(count)


