import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

circle_cordinate = []
stack = []

for _ in range(n):
    center, radious = map(int, input().split())
    circle_cordinate.append(('(', center-radious))
    circle_cordinate.append((')', center + radious))



# 원의 좌표들을 오름 차순으로 정렬 좌표가 같을시 ')' 표시가 '(' 보다 먼저 오게 정렬(-ord(x[0]))
circle_cordinate = sorted(circle_cordinate, key= lambda x:(x[1], -ord(x[0])))

answer = 1
for i in range(n*2):
    if not stack:
        stack.append([circle_cordinate[i][0], circle_cordinate[i][1], 0])
        continue

    if circle_cordinate[i][0] == '(':
        if stack[-1][1] == circle_cordinate[i][1]:
            stack[-1][2] = 1
            stack.append([circle_cordinate[i][0], circle_cordinate[i][1], 0])
        else:
            stack.append([circle_cordinate[i][0], circle_cordinate[i][1], 0])
    
    elif circle_cordinate[i][0] == ')':
        if stack[-1][2] == 0:
            answer += 1
        elif stack[-1][2] == 1:
            answer += 2

        stack.pop()

        if i != (n*2-1):
            if circle_cordinate[i+1][1] != circle_cordinate[i][1]:
                stack[-1][2] = 0

    
print(answer)

