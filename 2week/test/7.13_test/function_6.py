# 직사각형의 넓이를 구하시오.
# 직사각형의 세로는 n 가로는 m
# input 예시
# 10 20

n, m = map(int, input().split()) 

print(n*m)

# 내장함수를 10을 다 더해주는 함수가 있다
def plus10(n):
    return n +10

num = [10, 20, 30]
new_num = list(map(plus10, num))
print(new_num)

