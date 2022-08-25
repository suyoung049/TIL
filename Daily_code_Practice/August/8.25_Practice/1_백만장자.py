import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    list_ = list(map(int, input().split()))

    max_ = list_[-1]  # 리스트의 마지막 수를 최대값으로 지정[1,1,3,1,2]의 경우 2
    sum_ = 0          # 시세 차이를 더해줄 값을 지정
    for i in range(n-2, -1, -1):   # 마지막수가 최대값으로 지정 되었기 때문에 그 다음 수부터 0까지 거꾸로 순회
        if list_[i] >= max_:
            max_ = list_[i]       # 리스트의 수가 최대값 보다 크면 max 값 변경
        else:
            sum_ += (max_ - list_[i]) # 그렇지 않으면 max 값에서 리스트의 수 마이너스
    
    print(f'#{test_case} {sum_}')
