s = input()
y = (s[0:4])
m = (s[4:6])
d = (s[6:8])
if 0 < int(m) < 13:
    if int(m) == 1: 
        if int(d) < 32:
            print(y, m, d, sep = '/')
        else:
            print('-1')
    if int(m) == 2:
        if int(d) < 29:
             print(y, m, d, sep = '/')
        else:
            print('-1')
    if int(m) == 3:
        if int(d) < 32:
            print(y, m, d, sep = '/')
        else:
            print('-1')
    if int(m) == 4:
        if int(d) < 31:
            print(y, m, d, sep = '/')
        else:
            print('-1')
    # 단순 반복으로 각 월마다 12월 까지 월에 맞는 30일, 31일 조건식 만들면 됩니다
    # 단순 반복이라 생략......
else:
    print('-1')
           
    
     







   