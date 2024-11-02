import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

def pprint(matrix):
    for x in matrix:
        print(x)

n, m = map(int, input().split())
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 키가 작은 순서로 저장 
    matrix[a][b] = 1

# 키를 비교할수 있는 모든 사람 저장
for k in range(1, n +1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            if j == i:
                continue
            if not matrix[j][i]:
                if matrix[j][k] == 1 and matrix[k][i] == 1:
                    matrix[j][i] = 1

answer = 0
for j in range(1, n+ 1):
    people = 0
    for i in range(1, n+1):
        # j에 대해서 matrix[j][i] j보다 키가 큰 사람의수 matrix[i][j] j보다 키가큰 사람의수를 합친다
        people += (matrix[j][i] + matrix[i][j])
        # 만약 비교한 사람의수가 본인을 제외한 사람 수라면 정답에 더하기 
    if people == n-1:
        answer += 1

print(answer)