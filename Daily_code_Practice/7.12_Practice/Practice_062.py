num = [-10, -100, -30] # 최대값 구하기
# 1. 반복
max = -10000 # 데이터의 첫번째 값을 사용하면 편하다.
for i in num:
    if(i > max):   # 2. 만약, max값이 n보다 작으면 바꾼다
        max = i
print(max)