import sys
from heapq import heappush, heappop
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

# 문제의 핵심은 선물을 가장 많이 담고 있는 상자에서 먼저 원하는 아이들이 원하는 만큼 가져 가는 거

n, m = map(int, input().split())

present = list(map(int, input().split()))
child = list(map(int, input().split()))

check = True
heaq_present = []

# 선물 상자의 크기가 큰 순위로 heapq에 삽입
for i in range(n):
    heappush(heaq_present, (-present[i], present[i]))


for j in range(m):
    # 큰 선물 순으로 pop한 후에
    max_present = heappop(heaq_present)

    # 아이들 순서대로 원하는 선물보다 선물의 크기 크면
    if child[j] <= max_present[1]:
        change_present = max_present[1] - child[j]
        if change_present == 0:
            continue
        # 상자에서 선물을 뺀 값을 삽입
        heappush(heaq_present, (-change_present, change_present))
    
    # 선물 상자들 중에 아이들이 원하는 선물이 없으면 실패 표시
    else:
        check = False

if not check:
    print(0)
else:
    print(1)
        

