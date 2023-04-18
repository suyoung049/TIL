import sys
from heapq import heappop, heappush
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n = int(input())

country_1 = list(map(int, input().split()))
country_2 = list(map(int, input().split()))

country_1.sort()
heapque = []

for i in range(n):
    heappush(heapque, (-country_2[i], country_2[i]))

result = 0
for i in range(n):
    num_ = heappop(heapque)
    result += country_1[i] * num_[1]
print(result)