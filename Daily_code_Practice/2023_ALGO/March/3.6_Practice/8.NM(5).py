import sys
sys.stdin = open('8_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
num_li = list(map(int, input().split()))

rs = []
num_li.sort()




def recu(num_, i):
    if num_ == m:
        print(' '.join(map(str, rs)))
        return

    for j in range(i,n):
        check = [False] * n
        if check[j] == False:
            check[j] = True
            rs.append(num_li[j])
            recu(num_+1, j)
            check[j] = False
            rs.pop()

recu(0,0)