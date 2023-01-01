import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline
from collections import deque

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

while True:
    n, m = map(int, input().split())

    if (n, m) == (0, 0):
        break

    else:
        matrix = list(list(input().split()) for _ in range(m))
        pprint(matrix)