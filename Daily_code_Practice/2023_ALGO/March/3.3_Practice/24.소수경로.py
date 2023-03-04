import sys
sys.stdin = open('24_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

T = int(input())
for Test_case in range(T):
    start, end = map(int, input().split())

    prim = [True for _ in range(10000)]
    visit = [0 for _ in range(10000)]

    # 소수를 구하는 함수
    def check_prim():
        for i in range(2, int(10000*0.5)+1):
            if prim[i] == True:
                for j in range(2*i, 10000, i):
                    prim[j] = False

    def bfs():
        q = deque([(start,0)])
        visit[start] = 1

        while q:
            y, count_ = q.popleft()

            strNow = str(y)

            if y == end:
                return count_

            # 문제에서 주어진 각 자리수 마다 하나씩 바구는 로직
            for i in range(4):
                for j in range(10):
                    change = int(strNow[:i] + str(j) + strNow[i+1:])

                    if visit[change] == 0 and prim[change] == True and change >= 1000:
                        visit[change] = 1
                        q.append((change, count_ + 1))

    check_prim()

    result = bfs()

    if result == None:
        print('Impossible')
    else:
        print(result)
