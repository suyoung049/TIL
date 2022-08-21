import sys
sys.stdin = open('1_input.txt', 'r')

n = int(input())
stack = []
result = []
check = True

i = 1


for _ in range(n):
    num_ = int(input())
    while i <= num_:
        stack.append(i)
        result.append('+')
        i += 1
    if stack[-1] == num_:
        stack.pop()
        result.append('-')

    else:
        check = False
if check == False:
    print('NO')
else:
    for i in result:
        print(i)