import sys
sys.stdin = open('4_input.txt', 'r')

def pprint(list_):
    for row in list_:
        print(row)

T = 10

for test_case in range(1, T+1):

    n = int(input())
    rotated_matrix = [[0]*100 for _ in range(100)]

    matrix = [list(map(int, input().split())) for _ in range(100)]
    sum_ = []
    hap = 0

    for i in range(100):
        sum_.append(sum(matrix[i]))
        for j in range(100):
            if i == j:
                hap += matrix[i][i]

    sum_.append(hap)

    

    hap = 0
    for i in range(100):
        for j in range(100):
            rotated_matrix[i][j] = matrix[n-j-1][i]

    for i in range(100):
        sum_.append(sum(rotated_matrix[i]))
        for j in range(100):
            if i == j:
                hap += rotated_matrix[i][i]

    sum_.append(hap)

    print(f'#{test_case} {max(sum_)}')

    

