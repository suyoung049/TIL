import sys

sys.stdin = open("11652_input.txt")

n = int(input())
card_list = {}
for _ in range(n):
    num = int(input())
    if num in card_list:
        card_list[num] += 1
    else:
        card_list[num] = 1
max = 0
sor_card = dict(sorted(card_list.items()))
for i in sor_card:
    if sor_card[i] > max:
        max = sor_card[i]
        max_card = i

print(max_card)