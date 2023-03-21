import sys
sys.stdin = open('3_input.txt', 'r')
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

student_li = [[] for _ in range(n+1)]
tall = [0] * (n+1)

for _ in range(m):
    y, x = map(int, input().split())

    student_li[y].append(x)

    tall[x] += 1


result = []
def tall_li(q):

    while q:
        now = q.popleft()

        result.append(now)

        for j in student_li[now]:
            tall[j] -= 1

            if tall[j] == 0:
                q.append(j)


q = deque()
for i in range(1, n+1):
    if tall[i] == 0:
        q.append(i)

tall_li(q)

for i in result:
    print(i, end = ' ')
