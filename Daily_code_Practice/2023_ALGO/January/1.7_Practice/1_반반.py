import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

T = int(input())


for test_case in range(1, T+1):
    text = input()
    stack_1 = [text[0]]
    stack_2 = []

    for i in range(1, 4):
        if text[i] == stack_1[-1]:
            stack_1.append(text[i])
        
        elif not stack_2:
            stack_2.append(text[i])
        
        elif text[i] == stack_2[-1]:
            stack_2.append(text[i])

    a = len(stack_1)
    b = len(stack_2)
    
    print(f'#{test_case}', end = ' ')
    if a == 2 and b == 2:
        print('Yes')

    else:
        print('No')            