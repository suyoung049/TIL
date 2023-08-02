import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())

belt = list(map(int, input().split()))
robot = [0] * n

answer = 0
cnt = 0

while True:
    answer += 1

    belt = [belt[-1]] + belt[:-1]
    robot = [0] + robot[:-1]
    robot[-1] = 0

    for j in range(n-2, 0, -1):
        if robot[j+1] == 0 and robot[j] == 1 and belt[j+1] > 0:
            robot[j+1] = 1
            belt[j+1] -= 1
            robot[j] = 0
            
            if belt[j+1] == 0:
                cnt += 1

    if belt[0] > 0:
        belt[0] -= 1
        robot[0] += 1
        
        if belt[0] == 0:
            cnt += 1
    
    if cnt >= k:
        break


print(answer)