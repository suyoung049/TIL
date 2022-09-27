from collections import deque
import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline



n, m = map(int, input().split())


stay = [0] * 100001
check = [0] *100001

def move(now):
    data = []
    temp = now
    for _ in range(stay[now]+ 1):
        data.append(temp)
        temp = check[temp]
    print(data)
    print(' '.join(map(str,data[::-1])))


def bfs(y):
    
    q = deque([y])

    while q:
        
        y = q.popleft()

        if y == m:
            print(stay[y])

            move(y)
            return 

        for ny in (y+1, y-1, 2*y):
            if 0<= ny < 100001: 
                if stay[ny]== 0 or stay[ny] >= stay[y] + 1: # 재방문 가능 
                    check[ny] = y
                    stay[ny] = stay[y] + 1
                    q.append(ny)

bfs(n)





