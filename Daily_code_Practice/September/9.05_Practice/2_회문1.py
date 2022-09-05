import sys
sys.stdin = open('2_input.txt', 'r')

T = 10

for test_case in range(1, T+1):
    n = int(input())

    map=[list(input()) for _ in range(8)]
    map2 = [[0] * 8 for _ in range(8)]    
    for j in range(8):
        for i in range(8):

            map2[j][i] = map[8-i-1][j]
    
    count = 0

    for j in range(8):
        for i in range(8-n+1):
            if map[j][i:i+n] == map[j][i:i+n][::-1]:
                count += 1
    
    
            if map2[j][i:i+n] == map2[j][i:i+n][::-1]:
                count += 1

    print(f'#{test_case} {count}')

   