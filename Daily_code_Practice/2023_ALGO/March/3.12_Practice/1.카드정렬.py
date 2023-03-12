import sys
from heapq import heappop, heappush
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

card_dumy = []
temp = 0
answer = 0

for _ in range(n):
    card = int(input())

    heappush(card_dumy, card)


while True:
    if len(card_dumy) == 1:
        break

    for _ in range(2):
        dumy = heappop(card_dumy)
        temp += dumy

    answer += temp
    heappush(card_dumy, temp)
    temp = 0

print(answer)



