from collections import deque
import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline



n, m = map(int, input().split())
dy = [1, -1, 2]

stay = [0] *51
check = [0] *51

def move(now):
    data = []
    temp = now
    for _ in range(stay[now]+ 1):
        data.append(temp)
        temp = check[temp]
    print(' '.join(map(str,data[::-1])))


def bfs(y):
    
    q = deque([y])

    while q:
        
        y = q.popleft()

        if y == m:
            print(stay[y])

            move(y)
            return

        for i in range(3):
            if i < 2:
                ny = y + dy[i]

                if 0<= ny < 51 and check[ny] == 0:
                    check[ny] = y
                    stay[ny] = stay[y] + 1
                    q.append(ny)

            else:
                ny = y*dy[i]

                if 0<= ny < 51 and check[ny] == 0:
                    check[ny] = y
                    stay[ny] = stay[y] + 1
                    q.append(ny)
bfs(n)
print(stay)


