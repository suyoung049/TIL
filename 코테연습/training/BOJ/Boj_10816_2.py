import sys

sys.stdin = open("10816_input.txt", "r") 

N = int(input())
card = list(map(int, input().split()))
M = int(input())
num_ = list(map(int, input().split()))
check = dict()
for i in card:
    if i in check:
        check[i] += 1
    else:
        check[i] = 1
print(check)
for i in num_:
    if i in check:
        print(check[i], end = ' ')
    else:
        print(0, end = ' ')
