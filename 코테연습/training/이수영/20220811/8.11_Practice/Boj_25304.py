import sys

sys.stdin = open("25304_input.txt", "r")

total_money = int(input())

N = int(input())
buy_list = []

for _ in range(N):
    x, y = map(int, input().split())
    buy_money = x * y
    buy_list.append(buy_money)
buy = sum(buy_list)

if buy == total_money:
    print('Yes')
else:
    print('No')