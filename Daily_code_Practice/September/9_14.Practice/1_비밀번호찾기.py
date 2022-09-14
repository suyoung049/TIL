import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

dict_ = {}

for _ in range(n):
    k, v = input().split()
    dict_[k] = v

for _ in range(m):
    x = input().strip()
    print(dict_[x])
