import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
bishop_li = [[] for _ in range(2*n-1)]
check = [False] * (2 * n)

for j in range(n):
    for i in range(n):
        if matrix[j][i] == 1:
            bishop_li[j+i].append((j,i))

def dfs(b_n, cnt):
    global answer
    if answer >= (cnt + ((2*n-1) - b_n)//2):
        return
    if b_n >= (2 * n -1):
        answer = max(answer, cnt)
        return
    
    for b_j, b_i in bishop_li[b_n]:
        if check[b_j - b_i] == False:
            check[b_j - b_i] = True
            dfs(b_n+2, cnt+1)
            check[b_j - b_i] = False

    dfs(b_n+2, cnt)


answer = 0
dfs(0, 0)
t = answer
answer = 0
dfs(1, 0)
print(answer + t)