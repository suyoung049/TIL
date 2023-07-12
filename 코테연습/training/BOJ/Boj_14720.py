import sys

sys.stdin = open("1764_input.txt", "r")

N = int(input())
milk_store = list(map(int, input().split()))
milk = 0
coun = 0

for i in range(N):
    if milk_store[i] == milk:
        coun += 1
        milk += 1
    if milk > 2:
        milk = 0
print(coun)

