import sys
sys.stdin = open('1_input.txt','r')
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

n, m, b = map(int, input().split())
floor = 0   # 0층에서 부터 시작
time = sys.maxsize  # 걸리는 최소의 시간이므로 최대값 지정

matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(257):
    max_ , min_ = 0,0 # 블록을 빼야 하는 경우, 블록을 넣어야 하는 경우

    for j in range(n):
        for k in range(m):

            if matrix[j][k] >= i:
                max_ += matrix[j][k] - i  # 블록을 빼는 경우는 2초시간 발생
            
            else:
                min_ += i - matrix[j][k]  # 블록을 넣는 경우는 1초시간 발생
    
    if max_ + b >= min_:                   # 인벤토리의 블록의 수가 블록을 채우기에 충분할때
        if min_ + (max_*2) <= time:             
            time = min_ + (max_ * 2)           # 시간의 최소값 연산
            floor = i                             # 시간의 최소값 일때의 층

print(time, floor)



