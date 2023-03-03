import sys
sys.stdin = open('19_input.txt','r')

a, b = input().split()

re_a = ''
re_b = ''

for i in range(2 ,-1 ,-1):
    re_a += a[i]
    re_b += b[i]

re_a = int(re_a)
re_b = int(re_b)

print(max(re_a, re_b))