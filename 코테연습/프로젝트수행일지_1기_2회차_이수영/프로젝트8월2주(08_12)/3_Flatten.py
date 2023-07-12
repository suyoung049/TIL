import sys

sys.stdin = open("_Flatten.txt")



for test_case in range(1, 11):
    dump = int(input())
    box_list = list(map(int, input().split()))

    coun = [0] * 101  # 박스의 높이들을 저장할 리스트 
    for i in box_list:
        coun[i] += 1    # 박스 높이에 따른 수를 저장합니다.
    
    min_ = min(box_list)  # 가장 낮은 박스의 높이
    max_ = max(box_list)  # 가장 높은 박스의 높이
    
    n = 0                  
    while n < dump:            # 주어진 덤프의 수만큼 높이 조절을 진행하기 위한 조건문   
        coun[max_] -= 1        # 가장 높은 높이에서 하나를 가장낮은 높이로 옮기게 되면
        coun[max_-1] += 1      # 2번째 높은 박스 높이의 수가 1증가
        coun[min_] -= 1        # 마찬가지로 가장 낮은 박스의 높이는 박스를 하나 받아서 감소
        coun[min_+1] += 1      # 2번째로 낮은 박스의 높이의 수는 1증가 

        while coun[max_] == 0:   # dump를 진행하다 가장 높은 높이나 낮은 높이가 0이되면 
            max_ -= 1            # 다음 높은 높이나 낮은 높이로 변경하기 위한 조건문
        while coun[min_] == 0:
            min_ += 1

        n += 1                  # 덤프의 횟수를 증가 시켜 while 문을 종료시키기 위한 조건
    result = max_ - min_        # dump를 마친후 가장 높은 높이와 낮은 높이의 최종 차이
    print(f'#{test_case} {result}')

# 처음 2차원 리스트로 생각해서 많이 헤맸습니다. 다시 문제를 천천히 읽어보니 2차원 리스트를
# 활용하지 않고 높이의 개수를 정리하면 풀 수 있겠다고 방향을 완전히 바꾼것이 도움이
# 많이 되었습니다. 하지만 조건중에 주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없다
# 는 조건이 이해가 안되고, 어떤 코드를 어느 위치에 사용해야 하는지 모르겠습니다.
