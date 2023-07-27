import sys
from collections import deque
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


n = int(input())

matrix = [[0] * n for _ in range(n)]

like_frend = {}

for _ in range(n*n):
    people = list(map(int, input().split()))
    people = deque(people)
    me = people.popleft()

    like_frend[me] = people


for me in like_frend:
    
    empty_cnt, friend_cnt, change_y, change_x = -1, -1, 0, 0
    
    for y in range(n):
        for x in range(n):
            if matrix[y][x] != 0:
                continue
            
            check_empty, check_friend = 0, 0

            for i in range (4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0<= ny < n and 0<= nx < n:
                    if matrix[ny][nx] == 0:
                        check_empty += 1
                    elif matrix[ny][nx] in like_frend[me]:
                        check_friend += 1
                
            if check_friend > friend_cnt:
                change_y, change_x = y, x
                friend_cnt = check_friend
                empty_cnt = check_empty

            
            elif check_friend == friend_cnt and check_empty > empty_cnt:
                change_y, change_x = y, x
                empty_cnt = check_empty

    matrix[change_y][change_x] = me

ans = 0
for y in range(n):
    for x in range(n):
        cnt = 0

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<= ny < n and 0<= nx < n:
                if matrix[ny][nx] in like_frend[matrix[y][x]]:
                    cnt += 1
                
        
        if cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000

print(ans)