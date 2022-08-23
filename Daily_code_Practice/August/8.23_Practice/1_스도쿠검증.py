import sys
sys.stdin = open('1_input.txt', 'r')


def pprint(arr):
    for i in range(len(arr)):
        print(arr[i])

T = int(input())

for test_case in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]

    check = True
    for i in range(9):
        cnt_r = [0]*10
        cnt_c = [0]*10
        for j in range(9):
            cnt_r[matrix[i][j]] += 1
            cnt_c[matrix[j][i]] += 1

        for k in range(1, 10):
            if cnt_r[k] != 1:
                check = False
                break
            if cnt_c[k] != 1:
                check = False
                break
    for i in range(0,9,3):
        for j in range(0,9,3):
            cnt_x = [0] * 10
            for x in range(3):
                for y in range(3):
                    cnt_x[matrix[i+x][j+y]] += 1
            
            for k in range(1, 10):
                if cnt_x[k] != 1:
                    check = False
                    break
    print(f'#{test_case}', end = ' ')
    if check == True:
        print(1)
    else:
        print(0)

