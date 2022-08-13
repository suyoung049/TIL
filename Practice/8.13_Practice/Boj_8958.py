import sys

sys.stdin = open("8958_input.txt", "r")

T = int(input())

for test_case in range(T):
    quiz = list(input())
    count = 0
    score = 0
    for i in quiz:
        if i == 'O':
            count += 1
            score += count
        if i == 'X':
            count = 0
    print(score)
