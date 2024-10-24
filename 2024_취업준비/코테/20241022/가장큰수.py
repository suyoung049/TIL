numbers = [3, 30, 34, 5, 9]

def solution(numbers):
    # 1. 모든 수를 문자열로 변환
    numbers = list(map(str, numbers))

    # 2. x+y와 y+x를 비교하여 정렬
    # 4자리수 비교 이유는 주어진 number의 범위가 1000이하
    # 3 -> 3333
    # 30 -> 3030
    # 34 -> 3434
    # 5 -> 5555
    # 9 -> 9999
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    # 3. 정렬된 numbers를 이어붙인 뒤 반환
    answer = ''.join(numbers)

    # 0이 여러개일 경우, "000" 대신 "0"을 반환하도록 예외처리
    if answer[0] == '0':
        return '0'
    else:
        return answer

print(solution(numbers))