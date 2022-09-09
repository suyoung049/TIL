import sys
sys.stdin = open('2_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    word = list(input())
    text = list(input())
    count = 0

    for i in range(n):
        if word[i] == text[i]:

            count += 1
    
    print(count)