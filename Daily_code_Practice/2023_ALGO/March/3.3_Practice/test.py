import sys
from itertools import permutations
sys.stdin = open('test_input.txt','r')
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
op_num = list(map(int, input().split()))

operater = '+'*op_num[0] + '-'*op_num[1] + '*'*op_num[2] + '%' *op_num[3]

oper_perm = permutations(operater, n-1)
oper_perm = set(oper_perm)

result = []
for perm in oper_perm:
    
    answer = num_list[0]
    
    for i in range(1, n):
        if perm[i-1] == '+':
            answer += num_list[i]
        elif perm[i-1] == '-':
            answer -= num_list[i]
        elif perm[i-1] == '*':
            answer *= num_list[i]
        elif perm[i-1] == '%':
            # answer = int(answer/num_list[i])
            if answer < 0 and num_list[i]>0:
                answer = -1 * ((-1*answer)//num_list[i])
            
            elif answer > 0 and num_list[i] < 0:
                answer = -1 * (answer//(-1*num_list[i]))
            
            else:
                answer //= num_list[i]
    

    result.append(answer)
print(max(result))
print(min(result))


