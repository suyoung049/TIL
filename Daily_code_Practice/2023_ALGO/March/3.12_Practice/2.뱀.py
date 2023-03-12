import sys
sys.stdin = open('2_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())
matrix = [['.'] * n for _ in range(n)]

m = int(input())

for _ in range(m):
    y, x = map(int, input().split())
    matrix[y-1][x-1] = '*'

direction_dict = {}
k = int(input())

for _ in range(k):
    time, direction = input().split()
    direction_dict[int(time)] = direction


snack_direction = 0
snake = deque([(0,0)])
time = 0


while True:
    y, x = snake[-1]

    ny = y + dy[snack_direction]
    nx = x + dx[snack_direction]
    
    if 0 > ny or 0 > nx or ny > n-1 or nx > n-1 or (ny,nx) in snake:
        break

    elif matrix[ny][nx] == '*':
        snake.append((ny,nx))
        matrix[ny][nx] = '.'
    
    else:
        snake.popleft()
        snake.append((ny,nx))
    
    time += 1

    if time in direction_dict:
        curve = direction_dict[time]
    
        if curve == 'D':
            snack_direction = ((snack_direction + 1) % 4)
        
        elif curve == 'L':
            snack_direction = ((snack_direction + 3) % 4)
    
print(time + 1)
    

    



        



