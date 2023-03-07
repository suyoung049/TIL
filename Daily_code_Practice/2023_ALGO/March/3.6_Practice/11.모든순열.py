import sys
sys.stdin = open('11_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

num_li = list(range(1,n+1))

rs = []
check = [False] * (n+1) 


def recu(num_):
    if num_ == n:
        print(' '.join(map(str, rs)))
        return

    for j in range(1, n+1):
        if not check[j]:
            check[j] = True
            rs.append(j)
            recu(num_ + 1)
            check[j] = False
            rs.pop()
recu(0)



