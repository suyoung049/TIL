import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
num_li = list(map(int, input().split()))

num_li.sort()

rs = []
check = [False] * n

def recu(num_):
    if num_ == m:
        print(' '.join(map(str, rs)))
        return
            
    remember_num = 0
    for j in range(n):
        if not check[j] and remember_num != num_li[j]:
            check[j] = True
            remember_num = num_li[j]
            rs.append(num_li[j])
            recu(num_ + 1)
            rs.pop()
            check[j] = False

recu(0)
