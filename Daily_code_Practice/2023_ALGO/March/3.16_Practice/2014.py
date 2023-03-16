import sys
from heapq import heappush, heappop
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())

num_li = list(map(int, input().split()))
multi = []

for num_ in num_li:
    heappush(multi, num_)

count_ = 0
while True:
    if count_ == k:
        print(current)
        break

    current = heappop(multi)
    
    # 여기 어딘가 시간을 줄일수 있는 코드가 들어가야 할거 같은데 
    count_ += 1
    for num_ in num_li:
        current_multi = num_ * current
        if current_multi in multi:
            continue

        else:
            heappush(multi, current_multi)



