n = 15

def solution(n):
    answer = 0
    for num in range(1,n+1):
        count = find_division(num)
        if (count >= 3):
            answer += 1
    print(answer)
    return answer

# 약수의 개수를 찾는 함수
def find_division(n):
    count = 0
    for i in range(1, int(n**0.5) +1):
        if (n % i == 0):
            count += 1
            if i != n//i:
                count += 1
    return count

solution(n)