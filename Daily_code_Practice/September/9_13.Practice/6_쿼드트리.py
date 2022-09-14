import sys
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())

matrix = [list(map(int, input().strip())) for _ in range(n)]
pprint(matrix)

def quad(y,x,n):

    for j in range(y,y+n):
        for i in range(x,x+n):
            if matrix[y][x] != matrix[j][i]: # 4분면으로 나눈 후에 한분면이 전부 같지 않다면 재귀함수를 사용해서 다시 나누어주어야 한다.
                print('(', end = '')
                quad(y,x,n//2) # 제 1분면
                quad(y,x+n//2,n//2) # 제 2분면
                quad(y+n//2,x,n//2) # 제 3분면
                quad(y+n//2, x+n//2, n//2) # 제 4분면으로 나누는 입력 코드
                print(')', end = '')
                return    # 같은 수가 나올때까지 전부 리턴
    
    if matrix[y][x] == 0:    # 만약 한 분면이 전부 0이라면 0을 출력
        print('0',end = '')
        return
    
    else:
        print('1', end = '')   # 만약 한 분면이 전부 1이라면 1을 출력
        return

quad(0,0,n) # 처음 (0,0) 에서부터 시작