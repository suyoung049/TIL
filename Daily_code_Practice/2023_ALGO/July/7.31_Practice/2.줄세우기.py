import sys
from collections import deque
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

P = int(input())
for tc in range(1, P+1):
    lst = list(map(int, input().split()))[1:]

    cnt = 0
    for i in range(1, 20):
        for j in range(i):
            if lst[i]<lst[j]:
                cnt += 1
    print(f'{tc} {cnt}')
            



