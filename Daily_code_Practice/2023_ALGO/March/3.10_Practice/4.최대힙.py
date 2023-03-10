import sys
from heapq import heappop, heappush
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

num_li = []

for _ in range(n):
    num = int(input())

    if num == 0:
        if len(num_li) == 0:
            print(0)
        else:
            answer = heappop(num_li)
            print(answer[1])

    
    else:
        heappush(num_li, (-num, num))
