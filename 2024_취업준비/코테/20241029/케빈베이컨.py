import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())


inf = 1000000001

# 모든 지점에서 다른 모든 지점의 최단 경로를 저장할 2차원 그래프 
matrix = [[inf for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
                if j == i:
                     continue
                # 최소값 갱신
                matrix[j][i] = min(matrix[j][i], matrix[j][k] + matrix[k][i])

# 케빈 베이컨 수 저장할 리스트
kevin_li = [inf for _ in range(n+1)]

# 케빈 베이컨의 수 갱신
for j in range(1, n+1):
     sum_num = 0
     for i in range(1, n+1):
        if matrix[j][i] == inf:
               continue
        sum_num += matrix[j][i]
     kevin_li[j] = sum_num

min_num = min(kevin_li)
answer_li = []
# 케빈 베이컨의 수가 작은 후보들 저장
for idx in range(1, n+1):
     if kevin_li[idx] == min_num:
          answer_li.append(idx)

# index가 적은 값 출력
print(answer_li[0])


        
    