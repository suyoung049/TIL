import sys
sys.stdin = open('16_input.txt')

T = int(input())

for test_case in range(T):

    num_, text = input().split()

    num_ = int(num_)

    answer = ''

    for i in range(len(text)):
        answer += text[i] * num_
    
    print(answer)



