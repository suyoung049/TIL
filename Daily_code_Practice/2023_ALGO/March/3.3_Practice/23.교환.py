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

        if x == count_:
            answer = max(answer, y)
            continue

        n = list(str(y))

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



print(bfs(n, count_))