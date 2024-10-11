n = 3
def solution(n):
    matrix = [list(0 for _ in range(n) ) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 1

    print(matrix)
    return matrix


solution(n)