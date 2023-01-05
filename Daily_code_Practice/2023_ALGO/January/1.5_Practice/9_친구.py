import sys
input = sys.stdin.readline

n, m = map(int, input().split())

grap = [[] for _ in range(n)]
friend = [False for _ in range(n)]
result = False

for _ in range(m):
    a, b = map(int, input().split())

    grap[a].append(b)
    grap[b].append(a)


def dfs(s, num):
    global result
    if num == 4:
        result = True
        return

    for i in grap[s]:
        if not friend[i]:
            friend[i] = True
            dfs(i, num+1)
            friend[i] = False
        

for i in range(n):
    friend[i] = True
    dfs(i, 0)
    friend[i] = False
    if result:
        break


if result:
    print(1)

else:
    print(0)




