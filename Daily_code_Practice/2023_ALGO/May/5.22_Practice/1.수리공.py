import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

empty, length = map(int, input().split())

empty_li = list(map(int, input().split()))

empty_li.sort()

a = empty_li[0] - 0.5 + length
count_ = 1

for i in range(1, empty):
    if a > empty_li[i]:
        continue

    else:
        a = empty_li[i] -0.5 + length
        count_ += 1

print(count_)