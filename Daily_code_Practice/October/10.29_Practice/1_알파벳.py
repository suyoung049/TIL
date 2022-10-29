import sys
sys.stdin = open('1_input.txt', 'r')


T = int(input())

chr_ = 'abcdefghijklmnopqrstuvwxyz'

for test_case in range(1, T+1):
    cnt_ = 0
    alpa = input().strip()

    for i in range(len(alpa)):
        if alpa[i] == chr_[i]:
            cnt_ += 1
        else:
            break
    
    print(f'#{test_case} {cnt_}')
    


   
