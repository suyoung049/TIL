import sys
from collections import deque
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    n, m = map(int, input().split())
    list_ = list(map(int, input().split()))   
    count = 0
    q= deque(list_)

    while q:
        max_ = max(q)
        front = q.popleft()
        m -=1 # 앞에서 제거 되면 수가 당겨진다. 

        if max_ == front:
            count += 1 # 제거 되는 수 만큼 카운트
            if m < 0:  # 제거되는 수가 m이 0보다 작아야 원하는 수의 나가는 순서
                print(count)
                break
        else:
            q.append(front)
            if m < 0:
                m = len(q)-1 # 맨끝자리에서 다시시작

                