import sys

sys.stdin = open("11945_input.txt", "r")
N, M = map(int,(input().split()))

boong = [list(input()) for _ in range(N)]
boong_r = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        boong_r[i][(M-1) - j] = boong[i][j]
for i in range(N):
    for j in range(M):
        print(boong_r[i][j], end = '')
    print()