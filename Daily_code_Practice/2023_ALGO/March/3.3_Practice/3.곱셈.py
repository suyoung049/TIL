import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

a = int(input())
b = input()
length = len(b)
for i in range(2, -1, -1):
    c = int(b[i])
    print(a * c)

print(a * int(b))

