import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline



n, m = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]
check = [[-1] * m for _ in range(n)]

for j in range(n):
    cnt = 0
    for i in range(m):
        if matrix[j][i] == "c":
            check[j][i] = 0

            while True:
                ni = i + 1

                if 0<= ni < m:
                    if matrix[j][ni] != "c":
                        cnt += 1
                        check[j][ni] = cnt
                        i = ni

                    else:
                        cnt = 0
                        break
                
                else:
                    break

for i in check:
    print(*i)