import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

while True:
    lotto = list(map(int, input().split()))

    lotto_len = lotto.pop(0)
    if lotto_len == 0:
        break
    
    else:
        lotto.sort()
        

        rs = []
        check = [False] * lotto_len

        def rcur(num_, i):
            if num_ == 6:
                print(' '.join(map(str, rs)))
                return

            else:
                for j in range(i+1, lotto_len):
                    if check[j] == False:
                        rs.append(lotto[j])
                        rcur(num_+1, j)
                        check[j] = False
                        rs.pop()

        rcur(0, -1)
        print()

  