import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

def pprint(list_):
    for row in list_:
        print(row)

num_sum = [[0] * (n+1) for _ in range(n+1)]

for j in range(1, n+1):
    for i in range(1, n+1):
        num_sum[j][i] = num_sum[j][i-1] + num_sum[j-1][i] - num_sum[j-1][i-1] + matrix[j-1][i-1]

for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())

    answer = num_sum[y2][x2] - num_sum[y1-1][x2] - num_sum[y2][x1-1] + num_sum[y1-1][x1-1]

    print(answer)

