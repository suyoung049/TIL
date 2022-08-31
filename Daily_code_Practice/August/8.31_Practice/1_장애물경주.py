import sys
sys.stdin = open('1_input.txt','r')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    height_list = list(map(int, input().split()))

    up = [0]
    down = [0]

    for i in range(1,n):
        if height_list[i] > height_list[i-1]:
            up.append(height_list[i]-height_list[i-1])
        elif height_list[i] < height_list[i-1]:
            down.append(height_list[i-1] - height_list[i])
    print(f'#{test_case}', end = ' ')        

    print(max(up), max(down))