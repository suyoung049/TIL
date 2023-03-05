import sys
input = sys.stdin.readline


n = 4


pos = [0] * n # 열확인
flag_a = [False] * n  # 행확인
flag_b = [False] * ((n*2)-1) # 왼쪽 위 오른쪽 아래 양 방향 확인
flag_c = [False] * ((n*2)-1) # 오른쪽 위 왼쪽 아래 양 방향 확인 

rs = ''
answer = []
def put():
    global rs
    for i in range(n):
        rs += str(pos[i])
    answer.append(rs)
    rs = ''

def set(i):
    for j in range(n):
        if not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+(n-1)]:
            pos[i] = j
            if i == n-1:
                put()
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+(n-1)] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+(n-1)] = False

set(0)
print(answer)
print(len(answer))