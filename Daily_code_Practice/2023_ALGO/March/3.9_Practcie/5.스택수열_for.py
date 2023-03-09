import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

answer = []
stack = []
check = True


for i in range(n):
    if i == 0:
        check_i = int(input())

        for i in range(1, check_i + 1):
            stack.append(i)
            answer.append('+')
            count_ = check_i

        if stack[-1] == check_i:
            stack.pop()
            answer.append('-')
        else:
            check = False
    else:
        if count_ > check_i:
            if stack[-1] == check_i:
                stack.pop()
                answer.append('-')
            else:
                check = False
        else:
            for i in range(count_ + 1, check_i + 1):
                stack.append(i)
                answer.append('+')
                count_ = check_i
            
            if stack[-1] == check_i:
                stack.pop()
                answer.append('-')
    
            else:
                check = False


if not check:
    print('NO')

else:
    for i in answer:
        print(i)