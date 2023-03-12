import sys
from heapq import heappop, heappush
sys.stdin = open('10_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

num_li = []

for _ in range(n):
    num_ = int(input())

    if num_ != 0:
        heappush(num_li, (abs(num_), num_))
    
    else:
        if not num_li:
            print(0)
        else:   
            answer = heappop(num_li)
            print(answer[1])


    
