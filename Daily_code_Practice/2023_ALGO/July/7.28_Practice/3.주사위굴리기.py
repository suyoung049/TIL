import sys
sys.stdin = open("3_input.txt", "r")
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

n, m, y, x, k = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

dice = [0, 0, 0, 0, 0, 0, 0]

commend = list(map(int, input().split()))

answer = []


for dir in commend:
    
    dir = dir % 4

    if dir == 0:
        ny = y + dy[dir]
        nx = x + dx[dir]

        if 0<= ny < n and 0<= nx < m:
            dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
        
            if matrix[ny][nx] != 0:
                dice[6] = matrix[ny][nx]
                matrix[ny][nx] = 0
            else:
                matrix[ny][nx] = dice[6]
            
            answer.append(dice[1])
            y = ny
            x = nx
        else:
            continue     
        
    elif dir == 1:
        ny = y + dy[dir]
        nx = x + dx[dir]

        if 0<= ny < n and 0<= nx < m:
            dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
        
            if matrix[ny][nx] != 0:
                dice[6] = matrix[ny][nx]
                matrix[ny][nx] = 0
            else:
                matrix[ny][nx] = dice[6]
            
            answer.append(dice[1])
            y = ny
            x = nx
        else:
            continue
       
    elif dir == 2:
        ny = y + dy[dir]
        nx = x + dx[dir]

        if 0<= ny < n and 0<= nx < m:
            dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
        
            if matrix[ny][nx] != 0:
                dice[6] = matrix[ny][nx]
                matrix[ny][nx] = 0
            else:
                matrix[ny][nx] = dice[6]
            
            answer.append(dice[1])
            y = ny
            x = nx
        else:
            continue
    
    elif dir == 3:
        ny = y + dy[dir]
        nx = x + dx[dir]

        if 0<= ny < n and 0<= nx < m:
            dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
        
            if matrix[ny][nx] != 0:
                dice[6] = matrix[ny][nx]
                matrix[ny][nx] = 0
            else:
                matrix[ny][nx] = dice[6]
            
            answer.append(dice[1])
            y = ny
            x = nx
        else:
            continue

for i in answer:
    print(i)