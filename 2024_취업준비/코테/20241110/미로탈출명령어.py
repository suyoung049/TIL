from copy import deepcopy
n, m, x, y, r, c, k = 3, 4, 2, 3, 3, 1, 5

direction = ['d', 'l', 'r', 'u']
dx = {'u': -1, 'd': 1, 'l': 0, 'r': 0}
dy = {'u': 0, 'd': 0, 'l': -1, 'r': 1}

def dfs(start, path, k, r, c, n, m):
    global direction
    global dx
    global dy
    if k == 0 and start[0] == r and start[1] == c:
        return path
    
    k-=1
    for i in range(4):
        dire = direction[i]
        nx = start[0] + dx[dire]
        ny = start[1] + dy[dire]

        min_path = abs(nx-r) + abs(ny-c)
        
        if 0<= nx < n and 0<= ny < m:
            if k >= min_path and (k-min_path)%2 == 0:
                path += dire
                result = dfs((nx,ny),path, k, r, c, n, m)
                return result
        
    return None

def solution(n, m, x, y, r, c, k):

    min_path = abs(x-r) + abs(y-c)

    if k < min_path:
        return "impossible"

    if (k - min_path) % 2 != 0:
        return "impossible"
    
    path = ""
    start = (x-1, y-1)

    answer = dfs(start, path, k, r-1, c-1, n, m)

    if not answer:
        return "impossible"
    

    return answer


print(solution(n, m, x, y, r, c, k))