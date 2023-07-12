import sys

sys.stdin = open("input_1945.txt", "r")


def cal(N, x):
    while N % x == 0:
        N //= x
        res[x] += 1

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    res = {2: 0, 3: 0, 5: 0, 7: 0, 11:0}
    cal(N, 2)
    cal(N, 3)
    cal(N, 5)
    cal(N, 7)
    cal(N, 11)
    print(f'#{test_case} {" ".join(map(str, res.values()))}')
    


        
        

