import sys
input = sys.stdin.readline


def cal_per(total, win):
    win_per = int((win * 100)/total)
    return win_per


total, win = map(int, input().split())
win_per = cal_per(total, win)

start = 1
end = total + 1 # 일반적으로 더 큰 범위를 설정하여 탐색 범위를 확보합니다.
result = -1

while start <= end:
    mid = (start + end) // 2
    new_per = cal_per(total + mid, win + mid)

    if new_per > win_per:
        result = mid  # 이 때의 mid 값을 저장해둡니다.
        end = mid - 1  # 범위를 좁혀서 더 작은 mid 값을 탐색
    else:
        start = mid + 1  # 승률 변화가 없는 경우 더 큰 mid 값을 탐색


print(result)