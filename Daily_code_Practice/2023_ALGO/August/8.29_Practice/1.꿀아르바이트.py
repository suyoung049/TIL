import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
day_money = list(map(int,input().split()))

start_money = sum(day_money[:m])
max_money = start_money

for j in range(m, n):
    start_money = start_money + day_money[j] - day_money[j-m]
    if max_money < start_money:
        max_money = start_money

print(max_money)