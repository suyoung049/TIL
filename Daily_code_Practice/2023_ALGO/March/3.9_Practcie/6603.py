import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

while True:
    num_li = list(map(int, input().split()))

    n = num_li.pop(0)
    if n ==  0:
        break

    
    rs = []
    check = [False] * n

    def recu(num_, i):
        if num_ == 6:
            print(' '.join(map(str, rs)))
            return

        for j in range(i, n):
            if not check[j]:
                check[j] = True
                rs.append(num_li[j])
                recu(num_ + 1, j)
                check[j] = False
                rs.pop()

    recu(0, 0)
    print()
