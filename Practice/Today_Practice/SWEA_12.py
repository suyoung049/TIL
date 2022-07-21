n = int(input())

for i in range(1,n+1):
    s = str(i)             # 3, 6, 9, 포함 문자를 찾아야 하기 때문에 문자열 변환
    count = 0
    for num in s:
        if (num == '3') or (num == '6') or (num == '9'):  # 3, 6, 9 카운트
            count += 1      # 여러개일 경우 대비
    if count == 0:            # 없으면 그대로 출력
        print(i, end = ' ')    # 아직 들여쓰기 실력 부족, 상황파악 능력 부족
    else:
        print(count * '-', end = ' ')

    
