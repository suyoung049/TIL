import sys
from heapq import heappop, heappush
sys.stdin = open('11_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

answer = []
left_heap = []
righ_heap = []

for i in range(n):
    
    num_ = int(input())

    if len(left_heap) == len(righ_heap):
        heappush(left_heap, (- num_, num_))
    
    else:
        heappush(righ_heap, (num_, num_))
    

    if righ_heap and left_heap[0][1] > righ_heap[0][0]:
        min_ = heappop(left_heap)
        max_ = heappop(righ_heap)

        heappush(left_heap, (-max_[0], max_[0]))
        heappush(righ_heap, (min_[1], min_[1]))
    
    answer.append(left_heap[0][1])

for i in answer:
    print(i)


    


    