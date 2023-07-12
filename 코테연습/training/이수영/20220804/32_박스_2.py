import sys

sys.stdin = open("32_input.txt", "r")

T = int(input())
for test_case in range(T):
    box = 1
    emty  = 0
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(matrix)
    move = 0
    for x in range(M):
        for y in range(N-1, -1, -1):
            if matrix[y][x] == box:
                 # while y+1 != N and matrix[y+1][x] != box:
                while True:
                    if (y+1) == N:
                        break
                    if matrix[y+1][x] == box:
                        break
               
                    matrix[y][x] = emty
                    matrix[y+1][x] = box
                    y += 1  
                    move += 1
    print(move)
                
