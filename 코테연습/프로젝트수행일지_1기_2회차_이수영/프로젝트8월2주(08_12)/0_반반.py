import sys

sys.stdin = open("_반반.txt")

T = int(input())

for test_case in range(1, T+1):
    text = list(input())
    alpa_dict = {}

    for chr_ in text:
        if chr_ in alpa_dict:
            alpa_dict[chr_] += 1
        else:
            alpa_dict[chr_] = 1
    print(f'#{test_case}', end = ' ')

    if len(alpa_dict) != 2:
        print('No')
    else:
        print('Yes')            