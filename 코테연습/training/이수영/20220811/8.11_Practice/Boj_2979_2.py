import sys

sys.stdin = open("2979_input.txt", "r")

a, b, c = map(int, input().split())
time_table = [0] * 101
for _ in range(3):
    x, y = map(int, input().split())
    for j in range(x,y):
        time_table[j] += 1
money = 0
for i in time_table:
    if i == 1:
        money += a * i
    elif i == 2:
        money += b * i 
    elif i == 3:
        money += c * i 
print(money)