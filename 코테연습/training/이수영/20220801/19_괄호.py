import sys

sys.stdin = open("괄호_input.txt", "r") 

T = int(input())

for test_caes in range(1, T+1):
    brecket = list(input())
    left = brecket.count('(')
    right = brecket.count(')')
    
    if left == right:
        print('YES')
    else:
        print('NO')

# '(', ')'의 수가 같아도 쌍을 이루지 않는 경우가 있어서 이경우는 코드가 맞지 않다.