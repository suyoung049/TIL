import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)

N = factorial(n)

N = str(N)
coun = 0

for i in N[::-1]:
    if i != '0':
        break
    coun += 1

print(coun)
    