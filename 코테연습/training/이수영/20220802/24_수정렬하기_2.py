import sys
import heapq

sys.stdin = open("24_input.txt", "r")
input = sys.stdin.readline

N = int(input())
list_ = []
hea = []
heapq.heapify(hea)
for _ in range(N):
    list_.append(int(input()))
for i in range(len(list_)):
    heapq.heappush(hea, list_[i])
print(hea)
for j in range(len(hea)):
    print(heapq.heappop(hea))
