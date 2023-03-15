import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline


def solve(start, end):
    mid = (start + end)//2

    # 히스토그램의 너비가 1일 될때 까지 반으로 분할, 분할한 조각의 너비가 1이 되면 그 직사각형의 높이를 반환
    if start == end:
        return heigh[start]

    # 접점을 포함하는 사각형의 최대 넓이 계산

    # mid 와 mid + 1만 포함하는 경우(밑변의 길이 2)
    tempHeight = min(heigh[mid:mid+2])
    tempArea = tempHeight * 2

    # 그 외 길이 경우
    ll, rr = mid, mid + 1

    # ll과 rr이 모두 범위밖에 나가면 종료
    while True:
        if ll <= start and rr >= end:
            break
        # ll과 rr이 가리키는 높이를 비교해서, 더 높은쪽을 먼저 늘린다(넓이의 최대값을 구하기 위해)
        if rr < end and (ll == start or heigh[ll-1] < heigh[rr+1]):
            rr += 1
            tempHeight = min(tempHeight, heigh[rr])
        else:
            ll -= 1
            tempHeight = min(tempHeight, heigh[ll])
        
        tempArea = max(tempArea, tempHeight * (rr-ll + 1))

    # 왼쪽 분할, 오른쪽 분할, 그리고 점접을 포함하는 area 중에서 제일 큰값을 return
    return max(solve(start, mid), solve(mid+1, end), tempArea)

while True:
    heigh = list(map(int, input().split()))
    
    if heigh[0] == 0:
        break

    n = heigh[0]
    print(solve(1,n))
