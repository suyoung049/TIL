import sys
sys.stdin = open('12_input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    answer = list(input().strip()) 

    x = 0 # 현재점수
    y = 0 # 총점수
    
    for i in range(len(answer)):
        if answer[i] == 'O':
            x += 1
            y += x
        elif answer[i] == 'X':
            x = 0
    
    print(y)