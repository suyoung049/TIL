import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())


m = len(str(n))


def bfs(n, k):
    check = set()
    check.add((n,0))
    q = deque()
    q.append((n,0))
    result = 0

    while q:
        num_, count_ = q.popleft()
        if count_ == k:
            result = max(result, num_)
            continue
        
        num_ = list(str(num_))

        for j in range(m-1):
            for i in range(j+1,m):
                if j == 0 and num_[i] == '0':
                    continue
                num_[j], num_[i] = num_[i], num_[j]
                n_num = int(''.join(num_))

                if (n_num,count_+1) not in check:
                    q.append((n_num,count_+1))
                    check.add((n_num, count_+1))
                num_[j], num_[i] = num_[i], num_[j]
    
    return result if result else -1
print(bfs(n,k))
