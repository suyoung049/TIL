import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
num_li = list(map(int, input().split()))
num_li.sort()
visit = [False] * n
answer = []

def dfs(k, s, tlist):
    if k == m:
        answer.append(tlist)
        return
    
    prev = 0
    for j in range(s, n):
        if prev != num_li[j] and not visit[j]:
            visit[j] = True
            prev = num_li[j]
            dfs(k+1, j+1, tlist+[num_li[j]])
            visit[j] = False

        
dfs(0, 0, [])
for i in answer:
    print(*i)