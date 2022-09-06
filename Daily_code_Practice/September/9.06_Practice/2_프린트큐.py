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
        m -=1

        if max_ == front:
            count += 1
            if m < 0:
                print(count)
                break
        else:
            q.append(front)
            if m < 0:
                m = len(q)-1

                