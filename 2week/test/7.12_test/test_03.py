num = int(input())
if  num > 150: 
    if num > 300:
        print('실외활동을 자제')
    print('매우 나쁨')
elif num > 80:
    print('나쁨')
elif num > 30:
    print('보통')
else:
    if num < 0:
        print('음수')
    else:
         print('좋음')

print('미세먼지 확인 완료')