from itertools import permutations
import sys
sys.stdin = open('9_input.txt', 'r')


n = int(input())
k = int(input())
cards = []

for _ in range(n):
    card = input()
    cards.append(card)

result = set()

for i in permutations(cards, k):
    result.add(''.join(i))  # 숫자가 합쳐진 단계에서 중복이 존재할수 있음 string으로 중복제거 

print(len(result))