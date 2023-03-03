import sys



a, b, c, d = map(int, input().split())

y = c - a
x = d - b

print(min(a, b, y, x))