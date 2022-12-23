import sys
sys.stdin = open('9_input.txt', 'r')
input = sys.stdin.readline

T = int(input())

count = 0

for _ in range(T):
    stack = ''
    a = input()

    for i in range(len(a)):
        if a[i] not in stack:
            stack += a[i]

        else:
            if stack[-1] == a[i]:
                stack += a[i]
            
    if a == stack:
        count += 1
print(count)

    