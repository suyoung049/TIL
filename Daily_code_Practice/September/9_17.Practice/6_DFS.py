import sys
sys.stdin = open('6_input.txt', 'r')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m , k = map(int, input().split())

graph_list = [[] for _ in range(n+1)]
visit = [0] * (n+1)
count = 1

for _ in range(m):
    x , y = map(int, input().split())

    graph_list[x].append(y)
    graph_list[y].append(x)

for i in range(len(graph_list)):
    graph_list[i].sort()

def dfs(start):
    global count
    visit[start] = count
    
    for i in graph_list[start]:
        if visit[i] == 0:
            count += 1
            dfs(i)
            

dfs(k)

for i in range(n+1):
    if i!=0:
        print(visit[i])




    