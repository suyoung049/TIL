import sys
sys.stdin = open('12_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

rs = []
check = [False] * (n+1)

def recur(num_, i):
    if num_ == m:
        print(' '.join(map(str, rs)))
        return 
    
    for j in range(i+1, n+1):
        if check[j] == False:
            check[j] = True
            rs.append(j)
            recur(num_ + 1, j)
            check[j] = False
            rs.pop() 
recur(0,0)