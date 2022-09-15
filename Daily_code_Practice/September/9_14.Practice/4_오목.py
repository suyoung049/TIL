import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 1, -1]  # 오목은 아래, 왼쪽,  왼쪽 아래 대각선, 왼쪽 위 대각선으로 전부 탐색가능
dx = [1, 0, 1, 1]


n = 19
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for j in range(n):
    for i in range(n):

        if matrix[j][i] == 1 or matrix[j][i] == 2:

            for k in range(4):
                count = 1
                nj = j + dy[k]
                ni = i + dx[k]

                while True:
                    if not(0<= nj <n and 0<=ni<n):
                        break
                    if matrix[j][i] != matrix[nj][ni]:
                        break

                    count += 1

                    nj = nj + dy[k]
                    ni = ni + dx[k]

                    if count == 5:
                        p_j = j - dy[k]
                        p_i = i - dy[k]
                         # 육목 케이스 제거 조건문
                        if not(0<= p_j < n and 0 <= p_i < n) or matrix[j][i] != matrix[p_j][p_i] :
                         
                                print(matrix[j][i])
                                print(j+1, i+1)
                                
                                answer = matrix[j][i]

if answer == 0:
    print(matrix[j][i])


                



