import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

rs = []


def recu(num_,i):
    check = [False] * (n+1)
    if num_ == m:
        print(' '.join(map(str, rs)))
        return

    for j in range(i, n+1):
        if check[j] == False:
            check[j] = True
            rs.append(j)
            recu(num_+1, j)
            check[j] = False
            rs.pop()

recu(0,1)