import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

spot_li = []

for _ in range(n):
    y, x = map(int, input().split())
    spot_li.append((y,x))

# 먼저 X좌표가 가까운 점들끼리 비교를 하기 위해서 점들을 X 좌표 기준으로 오름차순 정렬
spot_li.sort()

inf = sys.maxsize

# 점들 사이의 거리를 구하는 함수
def get_dist(a,b):
    return (a[0]-b[0]) ** 2 + (a[1] - b[1]) ** 2


def solve(start, end):
    # 최소 단위인 별 한개가 되었을 때는 거리를 계산 할 수 없으므로 무한대를 출력
    if start == end:
        return inf
    
    # 두 점이 처음과 끝점에만 존재할때, 두점의 사이의 거리가 최소거리
    elif end - start == 1:
        return get_dist(spot_li[end], spot_li[start])
    
    else:
        mid = (start+end)//2
        # 최소단위가 아닐 때에는 중앙을 기준으로 왼쪽, 오른쪽으로 나눈 영역에서의 최솟값과 중앙값을 걸쳐서 생성된 영역에서의 
        # 최솟값 이 세 개의 값중의 최솟값을 반환한다.
        # 먼저 왼쪽과 오른쪽 영역에서 구한 최솟값 중 더 작은 값을 구한다.
        min_dist = min(solve(start, mid), solve(mid+1, end))
        target_li = []

        # 이제 m을 걸친(중간영엑에 걸친) 영역에서의 최솟값을 구한다.
        # 이제 가능한 점의 후보를 각 점의 x 좌표와 m의 x좌표의 거리가 min_dist 미만인 점들로 추릴 수 있다.
        # 최솟값을 찾아야 하기에 이미 min_dist 이상인 점들은 거리를 확인할 필요가 없기 때문에
        # m의 왼쪽, 오른쪽을 탐색해 나가면서 m의 x 좌표와의 거리가 min_dist 미만인 점들을 후보로 넣어준다.
        
        for i in range(mid, start-1, -1):
            if (spot_li[i][0] - spot_li[mid][0]) ** 2 < min_dist:
                target_li.append(spot_li[i])
            else:
                break
        
        for j in range(mid+1, end+1):
            if (spot_li[j][0]- spot_li[mid][0]) ** 2 < min_dist:
                target_li.append(spot_li[j])
            
            else:
                break
        
        # 이제 이 부분이 포인트이다. 여기서 후보 점들을 y 좌표 기준으로 정렬해준다. 이미 x 좌표는 비슷한 점들을 모았으니
        # y 좌표가 가까운 점들을 비교했을 때 최솟값을 구할 수 있기 때문이다.
        target_li = sorted(target_li, key=lambda x:x[1])

        # 이제 후보군 내 두점간 거리를 계산, 이때 계산된 거리가 min_dist보다 작다면 min_dist를 최솟값으로 갱신해준다.
        for i in range(len(target_li)-1):
            for j in range(i+1, len(target_li)):
                if (target_li[i][1] - target_li[j][1]) ** 2 < min_dist:
                    dist = get_dist(target_li[i], target_li[j])
                    min_dist = min(min_dist, dist)
                
                else:
                    break
        # 만약 계산된 거리가 min_dist보다 크거나 같다면 이후에 나오는 점들과의 거리도 min_dist보다 크거나 같으므로 for 문을 나간다
        # (y 좌표로 이미 정렬이 되어있기 때문에 이후의 값은 지금의 y 좌표와 크거나 같기 때문에)
        # 모든 탐색이 끝나면 최솟값으로 갱신된 min_dist를 반환한다.
        
        return min_dist

# 만약 같은 점이 존재한다면 거리의 최솟값은 0이므로 같은 점이 존재하는지 확인해주고 있다면 0을 반환
if len(spot_li) != len(set(spot_li)):
    print(0)

else:
    print(solve(0, len(spot_li)-1))