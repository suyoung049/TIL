import sys
sys.stdin = open('2_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    text_bord = [[0]*15 for _ in range(5)]
    
    matrix = [list(input()) for _ in range(5)]
    
    for i in range(5):
        for j in range(len(matrix[i])):
            text_bord[i][j] = matrix[i][j]
    
    say = ''

    for i in range(15):
        for j in range(5):
            if text_bord[j][i] != 0:
                say += text_bord[j][i]
            else:
                say += ''
    print(f'#{test_case} {say}')
