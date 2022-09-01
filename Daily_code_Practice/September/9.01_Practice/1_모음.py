import sys
sys.stdin = open('1_input.txt','r')


word = ['a','e','i','o', 'u']

T = int(input())
for test_case in range(1, T+1):
    text = list(input())
    result =''

    for chr in text:

        if chr in word:
            result += ''
        else:
            result += chr
    print(f'#{test_case} {result}')


