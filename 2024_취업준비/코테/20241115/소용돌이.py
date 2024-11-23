import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())

for y in range(r1, r2):
    for x in range(c1, c2):
        print(y, x)