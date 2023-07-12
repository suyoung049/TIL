import sys

sys.stdin = open("34_input.txt", "r")

N, M = map(int, input().split())

card = list(map(int, input().split()))

card_sum = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_ = card[i] + card[j] + card[k]

            if M >= sum_ > card_sum:
                card_sum = sum_
            if card_sum == M:
                break
print(card_sum)

            