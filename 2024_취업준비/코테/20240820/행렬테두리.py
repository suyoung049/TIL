rows, columns, queries = 6, 6, 	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]

def rotation(matrix, x1, y1, x2, y2):
    min_score = matrix[x1][y1]
    left_top = matrix[x1][y1]
   

    # 시작점이 변할 예정인걸 가져와야 해서 아래로 이동하면서 변경(이동해야할 점이 변경되면 안됨)
    for i in range(x1, x2):
        matrix[i][y1] = matrix[i+1][y1]
        if min_score > matrix[i+1][y1]:
            min_score = matrix[i+1][y1]
    # 마찬가지로 오른쪽으로 이동하면서 변경
    for j in range(y1, y2):
        matrix[x2][j] = matrix[x2][j+1]
        if min_score > matrix[x2][j+1]:
          min_score = matrix[x2][j+1]

    # 이번엔 반대로 아래에서 부터 올라 가면서 변경
    for i in range(x2, x1, -1):
        matrix[i][y2] = matrix[i-1][y2]
        if min_score > matrix[i-1][y2]:
            min_score = matrix[i-1][y2]

    # 마지막으로 왼쪽에서 부터 이동하면서 변경
    for j in range(y2, y1, -1):
        matrix[x1][j] = matrix[x1][j-1]
        if min_score > matrix[x1][j-1]:
            min_score = matrix[x1][j-1]

    matrix[x1][y1+1] = left_top
    
    return matrix, min_score
            
def solution(rows, columns, queries):
    answer = []
    matrix = list([r * columns + c + 1 for c in range(columns)] for r in range(rows) )
    for query in queries:
        x1, y1, x2, y2 = query[0] - 1, query[1] -1, query[2] - 1, query[3] - 1
        matrix, min_score = rotation(matrix, x1, y1, x2, y2)
        answer.append(min_score)
    
    return answer


solution(rows, columns, queries)