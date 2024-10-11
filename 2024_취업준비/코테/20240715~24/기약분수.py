def solution(numer1, denom1, numer2, denom2):
    

    result1 = (numer1 * denom2) + (numer2 * denom1)
    result2 = denom1 * denom2

    answer = [result1//gcd(result1, result2), result2//gcd(result1, result2)]
    return answer

# 최대 공약수 구하는 함수
def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
# 최소 공배수 구하는 함수
def ucd(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i