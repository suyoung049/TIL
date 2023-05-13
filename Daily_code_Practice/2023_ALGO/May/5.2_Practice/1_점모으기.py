import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

spot = []
y_spot = []
x_spot = []

for _ in range(m):
    y, x = map(int, input().split())
    spot.append((y-1,x-1))
    y_spot.append(y-1)
    x_spot.append(x-1)

y_spot.sort()
x_spot.sort()


spot_sum = 0
j, i = y_spot[len(y_spot)//2], x_spot[len(x_spot)//2]
for y, x in spot:
    spot_sum += (abs(y-j) + abs(x-i))

print(spot_sum)