# 딕셔너리에 값 추가 하여 모두 1이 채워지면 멈추는 코드를 
# 작성하려고 하였는데 잘 되지 않았습니다.
a = int(input())
result = {}
n = 10            # 예제에서 주어지지 않음 변수도 넣어야 하는 문제
for i in range(1, n+1):
    x = a * i
    s = str(x)    # 글자로 변환하는 개념은 잘 따라 갔으나
    for num in s:
        if not num in result:
            result[num] = 1
    while result[num] != 0:   # 아마 잘못된 명령어로 된 코드라서 나오지 않고 여기서 멈추었습니다.
        print(s)
    
        
    