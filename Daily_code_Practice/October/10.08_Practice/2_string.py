import sys
sys.stdin = open('2_input.txt', 'r')

T = 10


for test_case in range(1, T+1):

    a = input().split()
    search = input()
    text = input().strip()
   
    count_ = text.count(search)

    print(f'#{test_case} {count_}')
    