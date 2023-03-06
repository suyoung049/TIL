import sys
sys.stdin = open('4_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
check = [False] * n

res = sys.maxsize
def recu(num_, i):
    global res
    if num_ == n//2:
        our_team = 0
        vers_team = 0

        for i in range(n):
            for j in range(n):
                if check[i] and check[j]:
                    our_team += matrix[i][j]
                
                if not check[i] and not check[j]:
                    vers_team += matrix[i][j]
        
        res = min(res, abs(our_team-vers_team))
        return

    for j in range(i, n):
        if not check[j]:
            check[j] = True
            recu(num_ + 1,  j)
            check[j] = False

recu(0,0)
print(res)