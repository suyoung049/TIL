import sys
import heapq

sys.stdin = open("1927_input.txt", "r")
input = sys.stdin.readline

N = int(input())
list_ = []
heap = []
heapq.heapify(heap)
for _ in range(N):
    list_.append(int(input()))


for number in list_:
    if number != 0:
        heapq.heappush(heap, number)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))


   