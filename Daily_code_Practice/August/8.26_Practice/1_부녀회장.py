import sys
sys.stdin = open('1_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):

    k = int(input())
    n = int(input())

    list_ = []
    tem = [1]*n

    for i in range(1, n+1):
        list_.append(i)
    
    coun = 0
   
    while True:
        if coun > k:
            break
        else:
            for x in range(1,n):
                tem[x] = list_[x] + tem[x-1]
            coun += 1
        tem = list_
    
    print(list_[n-1])

