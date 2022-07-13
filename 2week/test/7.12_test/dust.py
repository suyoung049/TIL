num = int(input())
if  num > 150: 
    print('매우 나쁨')
elif num > 80:
    print('나쁨')
elif num > 30:
    print('보통')
elif num > 0:
    print('좋음')
else:
    print('음수 입니다.')
print('미세먼지 확인 완료') # 조건식을 동시에 검사하는 것이 아니라 순차적으로 비교

