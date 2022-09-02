import sys
sys.stdin = open('4_input.txt','r')


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for _ in range(10):
    T = int(input())
    check = 0

    map = [list(input()) for _ in range(16)]

    y, x = 0, 0

    for j in range(16):
        for i in range(16):

            if map[j][i] == '2':
                y, x = j, i

    stack = [(y,x)]
    while stack:
        ey, ex = stack.pop()

        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]

            if 0<=ny<16 and 0<=nx<16:

                if map[ny][nx] == '0':
                    stack.append((ny,nx))
                    map[ny][nx] = "check"
                
                elif map[ny][nx] == '3':
                    check = 1
                    stack.clear()
                    break
    
    print(f"#{T} {check}")

    