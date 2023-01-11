import sys
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

tree = list(map(int, input().split()))

start, end = 0, max(tree)

while True:
    if start > end:
        break

    else:
        mid = (start+end)//2

        sum_ = 0

        for i in tree:
            if i >= mid:
                sum_ += (i-mid)

        if sum_ >= m:
            start = mid + 1
        else:
            end = mid - 1

print(end)

