import sys
input = sys.stdin.readline


P = int(input())

for _ in range(P):
    N, M = map(int, input().split())
    num = M

    answer = 1
    mod1, mod2 = 1, 1
    while True:
        if mod1 % num == 0 and mod2 % num == 1:
            break

        answer += 1
        # 피사노 주기에 의해 mod1 , mod1 % num 두 수 모두 num으로 나눈 나머지는 같다.
        mod1, mod2 = mod2 % num , (mod1 + mod2) % num


    print(f"{N} {answer}")



