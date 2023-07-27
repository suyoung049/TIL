import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

gear_li = [[0, 0, 0, 0, 0, 0, 0, 0]]

for _ in range(4):
    gear_li.append(list(map(int, input().strip())))

top_li = [0, 0, 0, 0, 0]


rotation_num = int(input())
rotation_li = []

for _ in range(rotation_num):
    gear_num, rotation_direction = map(int, input().split())
    rotation_li.append((gear_num, rotation_direction))

for gear_num, rotation_direction in rotation_li:
    # 자기 자신 회전 리스트에 넣기 회전방향이 같으면 0, 회전방향이 반대면 1을 같이 추가
    temp_li = [(gear_num, 0)]

    # 오른쪽 방향 처리 (본인 3시 톱니와 오른쪽 6시 톱니의 값을 비교 톱니의 개수 index 8을 넘을 수도 있으므로 %8 처리)
    for i in range(gear_num+1, 5):
        if gear_li[i-1][(top_li[i-1] +2) % 8] != gear_li[i][(top_li[i] + 6) % 8]:
            # 기준 톱니바퀴와 같은 방향으로 도는 지 아니면 반대방향으로 도는지 확인 
            temp_li.append((i, (i-gear_num) % 2))
        else:
            break
    
    # 같은 방식으로 왼쪽 방향 처리
    for i in range(gear_num-1, 0, -1):
        if gear_li[i+1][(top_li[i+1] + 6) % 8] != gear_li[i][(top_li[i] + 2) % 8]:
            temp_li.append((i, (gear_num-i) % 2))
        else:
            break

    
    for j, root in temp_li:
        if root == 0:
            top_li[j] = (top_li[j] - rotation_direction + 8) % 8
        else:
            top_li[j] = (top_li[j] + rotation_direction + 8) % 8

answer = 0
for i in range(1, 5):
    if gear_li[i][top_li[i]] == 1:
        answer += 2 ** (i-1)

print(answer)
    
