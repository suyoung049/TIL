import sys

sys.stdin = open("6996_input.txt", "r")

N = int(input())

for _ in range(N):
    a, b = map(str, input().split())
   
    sor_a = sorted(list(a))
    sor_b = sorted(list(b))

    if sor_a == sor_b:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')
        