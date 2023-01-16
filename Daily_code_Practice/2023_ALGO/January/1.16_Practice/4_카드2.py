import sys
from collections import deque
sys.stdin = open('4_input.txt','r')
input = sys.stdin.readline

n = int(input())

card = []

for i in range(1,n+1):
    card.append(int(i))

card = deque(card)

while True:

    first = card.popleft()
    if len(card) == 1:
        break
    sec = card.popleft()
    card.append(sec)

print(*card)
