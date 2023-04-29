import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n = int(input())


start, end = map(int, input().split())

graph = [[] for _ in range(n+1)]
check = [False] * (n+1)


m = int(input())

for _ in range(m):
    y, x = map(int, input().split())

    graph[y].append(x)
    graph[x].append(y)


answer = False
def dfs(start, count_):
    global answer
    check[start] = True

    if start == end:
        answer = True
        print(count_)
        return

    for people in graph[start]:
        if not check[people]:
            dfs(people, count_ + 1)
    
count_ = 0
dfs(start, count_)
if answer == False:
    print(-1)





