import sys
sys.stdin = open('2_input.txt', 'r')

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))


first , end = 1, max(tree_list) # 이분 탐색을 위한 범위 지정
while first <= end:   # 이분탐색은 처음이 끝보다 커지면 종료
    mid = (first+end)//2   # 이분탐색의 미드 설정

    sum_ = 0          # 필요한 나무 길이 설정

    for i in tree_list:
        if i >= mid:         
            sum_ += (i-mid)    # 자른 후의 나무 길이들의 합
        
    if sum_ >= M:               # 합이 목표치 보다 작으면 처음을 가운데 +1
        first = mid +1
    else:
        end = mid -1             # 합이 목표치 보다 크면 끝을 가운데 +1

print(end)