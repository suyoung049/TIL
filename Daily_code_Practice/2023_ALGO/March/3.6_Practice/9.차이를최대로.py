import sys
sys.stdin = open('9_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))

rs = []
check = [False] * n

answer = 0
def ncur(num_):
    global answer
    if num_ == n:
        susik = 0
        for i in range(0, n-1):
            susik += abs(rs[i] - rs[i+1])
        answer = max(answer, susik)

    for i in range(n):
        if not check[i]:
            check[i] = True
            rs.append(num_list[i])
            ncur(num_ + 1)
            check[i] = False
            rs.pop()
ncur(0)
print(answer)