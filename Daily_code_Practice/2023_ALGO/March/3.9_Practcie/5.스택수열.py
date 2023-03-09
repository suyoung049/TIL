import sys
sys.stdin = open('5_input.txt', 'r')
input = sys.stdin.readline

n = int(input())

answer = []
stack = []
check = True

i = 1
for _ in range(n):
    check_i = int(input())

    while 1:
        if i > check_i:
            break
        
        stack.append(i)
        answer.append('+')
        
        i += 1

        

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

    



