import sys
from collections import deque
sys.stdin = open('8_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

card_li = list(range(1, n+1))

card_li = deque(card_li)


while True:
    if len(card_li) == 1:
        break

    card_li.popleft()
    card = card_li.popleft()
    card_li.append(card)


for i in card_li:
    print(i)