import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline


T = int(input())
prim = [True for _ in range(6001)]


def check_prim():
    for i in range(2, int(6000**0.5) + 1):
        if prim[i] == True:
            for j in range(2*i, 6001, i):
                prim[j] = False

check_prim()

for test_case in range(T):
    num_ = int(input())

    start_num = num_//2
    end_num = num_//2

    while True:
        if prim[start_num] == True and prim[end_num] == True:
            break
        else:
            start_num -= 1
            end_num += 1

    print(start_num, end_num)


