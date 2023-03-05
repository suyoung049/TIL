import sys
sys.stdin = open('23_input.txt', 'r')
from  collections import deque
input = sys.stdin.readline

n, count_ = map(int, input().split())

m = len(str(n))


def bfs(n, k):
    check = set()
    check.add((n, 0))
    q = deque()
    q.append((n, 0))
    answer = 0

    while q:
        y, x = q.popleft()

        if x == k:
            answer = max(answer, y)
            continue

        n = list(str(y))

        # 문제에서 주어진 수를 바꾸는 로직
        for i in range(m-1):
            for j in range(i+1, m):
                if i == 0 and n[j] == '0':
                    continue
                n[i], n[j] = n[j], n[i]
                nn = int(''.join(n))

                if (nn, x+1) not in check:
                    check.add((nn, x+1))
                    q.append((nn, x+1))
                n[i], n[j] = n[j], n[i]
    
    return answer



result = bfs(n, count_)

if result == 0:
    print(-1)
else:
    print(result)