N = int(input())
arrange = [0] * 10 # (0~ 9 까지의 리스트 생성)
i = 0
while True:
    if 0 in arrange:
        i += 1
        num = str(N*i)
        for j in range(len(num)): # num이 1234라면 '1', '2', '3', '4'로 쪼갬
            arrange[int(num[j])] += 1  # 리스트 안에 맞는 숫자가 있다면 1씩 오름
    else:
        break                      # 0~9 모든 숫자가 0이 아닐때 조건문 멈춤
print(num)