import sys
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

x, y = 0, 0

direction = ['R', 'U', 'L', 'D' ]  
direction_2 = ['R', 'D', 'L', 'U']

for _ in range(m):
    command = input().split()
    i = 0
    i_2 = 0
    k = ''
    

    if command[0] == 'TURN':
        if command[1] == '0':
            i += 1
            k = direction[i]
        
        if command[1] == '1':
            i_2 += 1         
            k = direction_2[i] 
            if i > 3:
                i = 0
            if i_2 > 3:
                i_2 = 0

    if command[0] == 'MOVE':
        if k == 'R' or not k:
            x += int(command[1])
        
        if k == 'U':
            y += int(command[1])

        if k == 'L':
            x -= int(command[1])
        if k == 'D':
            y -= int(command[1])

    if x>n or y>n:
        break

       
    


