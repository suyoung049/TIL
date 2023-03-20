import sys
sys.stdin = open('1_input.txt', 'r')
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())

heavy_graph = [[] for _ in range(n+1)]
light_graph = [[] for _ in range(n+1)]


for _ in range(m):
    y, x = map(int, input().split())

    light_graph[y].append(x)
    heavy_graph[x].append(y)


def dfs_light(start):
    global l_count
    light_check[start] = True

    for j in light_graph[start]:
        if not light_check[j]:
            l_count += 1
            dfs_light(j)
    
    

def dfs_heavy(start):
    global h_count
    
    heavy_check[start] = True

    for j in heavy_graph[start]:
        if not heavy_check[j]:
            h_count += 1
            dfs_heavy(j)
   
    

marble = 0
for i in range(1, n+1):

    heavy_check = [False] * (n+1)
    light_check = [False] * (n+1)

    l_count = 0
    h_count = 0
    
    dfs_light(i)
    dfs_heavy(i)

    if l_count >= (n//2) + 1 or h_count >= (n//2) + 1:
        marble += 1


print(marble)
