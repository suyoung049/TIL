import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

rs = []


def recur(num):
    check = [False for _ in range(n+1)]
    if num == m:
        print(' '.join(map(str, rs)))
        return
    
    for i in range(1, n+1):
        if check[i] == False:
            check[i] = True
            rs.append(i)
            recur(num+1)
            check[i] = False
            rs.pop()

recur(0)