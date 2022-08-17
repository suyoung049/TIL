import sys

sys.stdin = open('4_input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    numbers = []
    solution = []
    print(f'#{test_case}')

    for i in range(N):
        numbers.append(1)
        solution.append(1)
        if i < 2:
            pass
        else:
            for j in range(1, len(numbers)-1):
                solution[j] = numbers[j-1] + numbers[j]
        for j in range(len(numbers)):
            numbers[j] = solution[j]
            print(str(numbers[j]) , end = ' ')
        print()