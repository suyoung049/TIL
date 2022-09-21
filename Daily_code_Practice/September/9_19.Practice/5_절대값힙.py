import sys
import heapq
sys.stdin = open('5_input.txt', 'r')

n = int(input())

num_list = []

for i in range(n):
    a = int(input())

    if a == 0:
        if num_list:
            print(heapq.heappop(num_list)[1])
        
        else:
            print(0)

    else:
        heapq.heappush(num_list, (abs(a), a))
