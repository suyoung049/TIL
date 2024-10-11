a = 4
b = 4
c = 4

def solution(a, b, c):
    if (a == b == c):
        print('전부 동일')
        print((b**3))
        answer = (a + b + c) + (a**2 + b**2 + c**2) + (a**3 + b**3 + c**3)
    elif (a != b and b!=c and a !=c):
        print("세개 다름")
        answer = (a + b + c)
    elif (a == b != c or a == c != b or c == b != a):
        print("두개 다름")
        answer = (a + b + c) + (a**2 + b**2 + c**2)
    print(answer)
    return answer

solution(a, b, c)