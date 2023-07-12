import sys

sys.stdin = open("2711_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, text = input().split()
    N = int(N)
    
    for i in range(len(text)):
        if i == (N-1):
            print('', end = '')
        else:
            print(text[i], end ='')
    print()
 
    
    
 