import sys
sys.stdin = open('2_input.txt', 'r')

T = int(input())

di = [0, 1, 0, -1]   # 델타 탐색 달팽이 모양으로 왼쪽, 아래족, 오른쪽, 위로 동장
dj = [1, 0, -1, 0]

for test_case in range(1, T+1):
    n = int(input())
    matrix = [[0]*n for _ in range(n)] # 달팽이 숫자가 들어갈 2차원 리스트

    lenth = 0
    i, j = 0, 0

    for x in range(1, (n*n) +1):

        matrix[i][j] = x

        i += di[lenth]      # 델타 탐색 왼쪽 먼저 진행
        j += dj[lenth]

        if  i < 0 or j < 0 or i >= n or j >= n or matrix[i][j] != 0: #델타 탐색 중지 조건 i, j 의 범위를 넘어가거나 이미 숫자가 들어가 있는 경우
            i -= di[lenth]                                 # 델타 탐색을 중지하고 다음 델타 탐색으로 이동
            j -= dj[lenth]

            lenth = (lenth+1) % 4 # 중지 조건을 만났을 때 다음 델타 탐색으로 넘어가기위한 조건문

            i += di[lenth]
            j += dj[lenth]  # 델타 탐색의 다음인 아래쪽 진행
    
    print(f'#{test_case}')
    for j in range(n) :
        for k in range(n) :
            print(matrix[j][k], end=' ')
        print()



     
     