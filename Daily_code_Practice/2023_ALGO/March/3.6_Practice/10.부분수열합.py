import sys
sys.stdin = open('10_input.txt', 'r')
input = sys.stdin.readline

n, s = map(int, input().split())

num_li = list(map(int, input().split()))


rs = []
check = [False] * n


def ncur(num_, i, k):
    global count_
    if num_ == k:
        if sum(rs) == s:
            count_ += 1  
        return

    for j in range(i, n):
        if not check[j]:
            check[j] = True
            rs.append(num_li[j])
            ncur(num_+1, j, k)
            check[j] = False
            rs.pop()

count_ = 0
for i in range(1, n+1):
    ncur(0, 0, i)

print(count_)