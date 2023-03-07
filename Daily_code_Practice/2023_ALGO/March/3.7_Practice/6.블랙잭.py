import sys
from itertools import combinations
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

card_li = list(map(int, input().split()))

answer = sys.maxsize
result = 0
for i in combinations(card_li, 3):
    card_sum = sum(i)
 
    if card_sum <= m:
        if answer > m -card_sum:
            answer = m-card_sum
            result = card_sum
    
print(result)

