import sys
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
count = 0

while True:
    y = int(n**(1/2))
    if y <= 1:
        count += n
        break
    n = n - y**2
    count += 1

print(count)

