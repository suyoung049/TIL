import sys
sys.stdin = open('2_input.txt',  'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    stone_list = list(map(int, input().split()))
    lenth = []
    for stone in stone_list:
        stone = abs(stone)
        lenth.append(stone)
    min_ = min(lenth)
    coun = lenth.count(min_)
    print(f'#{test_case}', end = ' ')
    print(min_, coun)