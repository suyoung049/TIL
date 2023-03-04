import sys
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

def fact(n):
    if n > 0:
        return n * fact(n-1)
    else:
        return 1

print(fact(n))