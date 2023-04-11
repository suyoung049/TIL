import sys
sys.stdin = open('1_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n, m = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]
check = [[[[-1] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]


def bfs(double_coin):
    q = deque([double_coin[0][0], double_coin[0][1], double_coin[1][0], double_coin[1][1]])

    # while q:

















double_coin = []
for j in range(n):
    for i in range(m):
        if matrix[j][i] == "o":
            double_coin.append((j,i))

bfs(double_coin)