import sys

sys.stdin = open("6996_input.txt", "r")

N = int(input())

for _ in range(N):
    a, b = map(str, input().split())
    a_list = list(a)
    b_list = list(b)

    if len(a_list) == len(b_list):
        for chr_ in a_list:
            if chr_ in b_list:
                b_list.remove(chr_)
                if not b_list:
                    print(f'{a} & {b} are anagrams.')
            else:
                print(f'{a} & {b} are NOT anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.') 