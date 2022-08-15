import sys

sys.stdin = open("1018_input.txt", "r")


def pprint(arr):
    for i in range(len(arr)):
        print(arr[i])

N, M = map(int, (input().split()))

matrix = [list(input()) for _ in range(N)]
count_ = []
for i in range(N-7):
    for j in range(M-7):
        count_w = 0
        count_b = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if matrix[x][y] != 'W':  # 시작점이 W일때
                        count_w += 1
                    if matrix[x][y] != 'B':  # 시작점이 B일때
                        count_b += 1
                else:
                    if matrix[x][y] != 'B':  # 시작점이 W일때
                        count_w += 1      
                    if matrix[x][y] != 'W':  # 시작점이 B일때
                        count_b += 1
        count_.append(count_w)
        count_.append(count_b)
print(min(count_))

