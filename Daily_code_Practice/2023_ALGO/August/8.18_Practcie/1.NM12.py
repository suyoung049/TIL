import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
num_li = list(map(int, input().split()))

num_li.sort()
answer = []
def dfs(k, s, tlist):
    if k == m:
        answer.append(tlist)
        return
    
    prev = 0

    for i in range(s, n):
        if prev != num_li[i]:
            prev = num_li[i]
            dfs(k+1, i, tlist + [num_li[i]])

dfs(0, 0, [])

for j in answer:
    print(*j)