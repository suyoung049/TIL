import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)
n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
a, b, c, = 0, 0, 0
def paper(y, x, n):
    global a
    global b
    global c
    check = matrix[y][x]

    for j in range(y, y+n):
        for i in range(x, x+n):
            if check != matrix[j][i]:
                for k in range(3):
                    for t in range(3):
                        paper(y+n//3*k, x+n//3*t, n//3) # 3으로 분할 할때는 9번 재귀함수로 분할 필요
                return                                  # 반복문으로 설정해서 구해준다.

    if check == -1:
        a += 1
        return
    if check == 0:
        b += 1
        return
    else:
        c += 1
        return


paper(0,0,n)
print(a)
print(b)
print(c)
