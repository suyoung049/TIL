numbers = [1, 1, 1]
target = 3
answer = 0
def solution(numbers, target):
    global answer
    length = len(numbers)
    dfs(0, length, numbers, 0, target)  # 초기 상태로 dfs 시작
    return answer   # 결과값을 리턴 (sum_list에 저장된 값들)

def dfs(idx, length, numbers, current_sum, target):
    global answer
    # 길이의 끝에 도달하면 sum_list에 현재 합계 추가
    if idx == length:
        if current_sum == target:
            answer += 1
        return
    
    # 현재 숫자를 더하거나 뺀 경우 모두 재귀 호출
    for j in [-1, 1]:
        dfs(idx + 1, length, numbers, current_sum + (numbers[idx] * j), target)

# 테스트 실행
result = solution(numbers, target)
print(result)