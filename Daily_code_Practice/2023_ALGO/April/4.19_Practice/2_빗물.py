import sys
sys.stdin = open("2_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = list(map(int, input().split()))

result = 0
for j in range(1, m-1):
    left_side = []
    right_side = []
    for i in range(0, j):
        left_side.append(matrix[i])
        for k in range(j+1, m):
            right_side.append(matrix[k])
    
    left_max = max(left_side)
    right_max = max(right_side)

    rain = min(left_max, right_max)

    if rain > matrix[j]:
        result += rain - matrix[j]

print(result)



