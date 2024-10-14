import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())

k = int(input())

matrix = [list(input().strip()) for _ in range(n)]
print(matrix)


I = [[0] * (m+1) for _ in range(n+1)]
J = [[0] * (m+1) for _ in range(n+1)]
O = [[0] * (m+1) for _ in range(n+1)]

for j in range(n):
    for i in range(m):
        I[j+1][i+1] = I[j+1][i] + I[j][i+1] - I[j][i]
        J[j+1][i+1] = J[j+1][i] + J[j][i+1] - J[j][i]
        O[j+1][i+1] = O[j+1][i] + O[j][i+1] - O[j][i]

        if matrix[j][i] == "J":
            J[j+1][i+1] += 1
        elif matrix[j][i] == "I":
            I[j+1][i+1] += 1
        else:
            O[j+1][i+1] += 1
    
print(J)
for _ in range(k):
    answer = []
    sj, si, ej, ei = map(int, input().split())
    j_result = J[ej][ei] - J[sj-1][ei] - J[ej][si-1] + J[sj-1][si-1]
    answer.append(j_result)
    o_result = O[ej][ei] - O[sj-1][ei] - O[ej][si-1] + O[sj-1][si-1]
    answer.append(o_result)
    i_result = I[ej][ei] - I[sj-1][ei] - I[ej][si-1] + I[sj-1][si-1]
    answer.append(i_result)


    print(*answer)