import sys
sys.stdin = open('12_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

num_li = list(map(int, input().split()))
num_li.sort()

rs = []
check = [False] * n


def recu(num_, i):
    if num_ == m:
        print(' '.join(map(str, rs)))
        return

    for j in range(i, n):
        if not check[j]:
            check[j] = True
            rs.append(num_li[j])
            recu(num_ + 1, j)
            check[j] = False
            rs.pop()

recu(0, 0)