import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline


res = int(input())
while True:
    op = input()
    if op == '=':
        break
    n = int(input())
    if op == '+': res += n
    elif op == '-': res -= n
    elif op == '*': res *= n
    elif op == '/': res //= n

print(res)

