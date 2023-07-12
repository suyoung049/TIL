n = int(input())
card = list(range(1, n + 1))

while len(card) > 1:
    print(card.pop(0), end = ' ')
    card.append(card.pop(0))

print(card[0])


