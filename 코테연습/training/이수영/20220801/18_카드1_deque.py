from collections import deque
n = int(input())
card = deque(range(1, n+1))

while len(card) > 1:
    print(card.popleft(), end = ' ')
    card.append(card.pepleft())

print(card[0])