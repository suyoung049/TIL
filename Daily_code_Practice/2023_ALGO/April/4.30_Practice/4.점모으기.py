import sys
sys.stdin = open("4_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())


spot = []

for _ in range(m):
    y, x = map(int, input().split())
    spot.append((y-1,x-1))

result = sys.maxsize

for j in range(n):
    for i in range(n):
        spot_sum = 0

        for y, x in spot:
            spot_sum += (abs(y-j) + abs(x-i))

        result = min(result, spot_sum)

print(result)