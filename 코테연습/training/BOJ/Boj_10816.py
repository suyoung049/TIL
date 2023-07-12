import sys

sys.stdin = open("10816_input.txt", "r") 

N = int(input())
card = list(map(int, input().split()))
M = int(input())
num_ = list(map(int, input().split()))
check = dict()
for i in range(M):
    check[num_[i]] = 0
for i in range(N):
    if card[i] in check:
        check[card[i]] += 1
print(" ".join(map(str, check.values())))
for i in check:
    print(check[i], end =' ')
