import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
sort_list = sorted(num_list)

weight = 1

for num in sort_list:
    if weight < num:
        break
    else:
        weight += num
       
answer = weight        
print(answer)


