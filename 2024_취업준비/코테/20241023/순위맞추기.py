n = 5
results = 	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
def solution(n, results):
    answer = 0
    score = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for y, x in results:
        score[y][x] = 1

    # i->k->j 에서 i->j의 새로운 엣지를 생성하면,
    # i와 j 를 참조하는 다른 정점들을 다시 검사해야 합니다.
    # 하지만 i나 j가 제일 제일 바깥쪽 for에 위치하게 되면, 지나간 i나 j 를 다시 검사할 수 없습니다.
    # 따라서 for의 순서는 k, i, j, 혹은 k, j, i 순서가 되어야 합니다.
    
    for k in range(1, n+1):
        for j in range(1, n+1):
            for i in range(1, n+1):
                if score[j][k] == 1 and score[k][i] == 1:
                    score[j][i] = 1
    
    for j in range(1, n+1):
        result = 0
        for i in range(1, n+1):
            result += (score[j][i] + score[i][j])
        if result == n-1:
            answer += 1
            
    return answer

print(solution(n, results))