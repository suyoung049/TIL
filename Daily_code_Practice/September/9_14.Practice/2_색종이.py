import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
w, b = 0, 0
def paper(y,x,n):
    global w
    global b

    for i in range(y, y+n):
        for j in range(x, x+n):
            if matrix[y][x] != matrix[i][j]:
                paper(y, x, n//2)
                paper(y, x+n//2, n//2)
                paper(y+n//2, x, n//2)
                paper(y+n//2, x+n//2, n//2)
                return


    if matrix[y][x] == 0:
        w += 1
        return
         
    else:
        b += 1
        return
        

paper(0,0,n)


print(w)
print(b)