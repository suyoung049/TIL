import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline


n, m = map(int, input().split())

rs = []
check = [False] * (n+1)


def rcur(num_, i):
    if num_  == m:
        print(' '.join(map(str, rs)))
        return

    else:
        for j in range(1+i, n+1):
            if not check[j]:
                rs.append(j)
                rcur(num_ + 1, j)
                check[j] = False
                rs.pop()

rcur(0,0)