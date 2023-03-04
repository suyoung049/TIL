import sys
sys.stdin = open('22_input.txt', 'r')

N = int(input())

num_list = list(map(int, input().split()))
prim = [True for _ in range(1001)]


def check_prim():
    for i in range(2, int(1000*0.5) + 1):
        if prim[i] == True:
            for j in range(2*i, 1001, i):
                prim[j] = False

check_prim()

count_ = 0

for num_ in num_list:
    if prim[num_] == True:
        count_ += 1
    if num_ == 1:
        count_ -= 1

print(count_)