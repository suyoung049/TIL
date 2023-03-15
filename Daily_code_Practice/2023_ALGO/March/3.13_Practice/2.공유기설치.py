import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n, c = map(int, input().split())

home_location = []

for _ in range(n):
    location = int(input())
    home_location.append(location)

home_location.sort()

start = 1
# 설치거리 이기 때문에 최대거리에서 이분 탐색
end = home_location[-1] - home_location[0]

while True:
    answer = []
    
    if start > end:
        break

    mid = (start+end)//2

    for i in range(len(home_location)):
        if i == 0:
            answer.append(home_location[i])


        elif home_location[i] >= answer[-1] + mid:
            answer.append(home_location[i])
    
    # 만약 설치수가 c 보다 작으면 갭을 줄여야함
    if len(answer) >= c:
        gap = mid
        start = mid + 1

    else:
        end = mid - 1

print(gap)
