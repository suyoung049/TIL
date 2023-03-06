import sys
sys.stdin = open('7_input.txt', 'r')
input = sys.stdin.readline

L, C = map(int, input().split())

alpa = list(input().split())
consonant = ['a', 'e', 'i', 'o', 'u']

alpa.sort()

rs = ''
check = [False] * C


def recu(num_, i):
    global rs
    if num_ == L:
        vo, co = 0, 0

        for i in range(L):
            if rs[i] in consonant:
                vo += 1
            else:
                co += 1

        # 모음 1개 이상, 자음 2개 이상
        if vo >= 1 and co >= 2:
            print("".join(rs))
        return

    for j in range(i, C):
        if not check[j]:
            check[j] = True
            rs += alpa[j]
            recu(num_+1, j)
            check[j] = False
            rs = rs[:-1]

recu(0,0)


    