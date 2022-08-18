import sys
sys.stdin = open('5_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    text = input()
    result = 0
    for i in range(1, len(text)):
        if text[i] == text[0]:
            if text[:i] == text[i:(i*2)]:
                result = i
                break
        
        
    print(f'#{test_case} {result}')
