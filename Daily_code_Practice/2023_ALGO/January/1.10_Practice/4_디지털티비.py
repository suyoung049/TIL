import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

chanel = []
answer =''

for _ in range(n):
    ch = input().strip()
    chanel.append(ch)

k1 = chanel.index('KBS1')
k2 = chanel.index('KBS2')

if k1 > k2:
    k2 += 1

answer += '1'* k1 + '4'* k1 + '1' * k2 + '4' * (k2-1)

print(answer)

