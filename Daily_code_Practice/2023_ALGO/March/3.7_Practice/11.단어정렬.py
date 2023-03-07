import sys
sys.stdin = open('11_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

chr_set = {}

for _ in range(n):
    chr_ = input().strip()
    chr_set[chr_] = len(chr_)


chr_set = dict(sorted(chr_set.items(), key = lambda x : (x[1], x[0])))

for i in chr_set:
    print(i)

