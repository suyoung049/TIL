import sys
sys.stdin = open('4_input.txt','r')
input = sys.stdin.readline

n = int(input())

num_li = list(map(int, input().split()))
operator = list(map(int, input().split()))


max_value = -1 * sys.maxsize
min_value = sys.maxsize
def dfs(depth, num_sum, plus, minus, multi, divide):
    global max_value
    global min_value

    if depth == n:
        max_value = max(max_value, num_sum)
        min_value = min(min_value, num_sum)
        return

    if plus:
        dfs(depth+1, num_sum + num_li[depth], plus-1, minus, multi, divide)
    
    if minus:
        dfs(depth+1, num_sum - num_li[depth], plus, minus-1, multi, divide)
    
    if multi:
        dfs(depth + 1, num_sum*num_li[depth],  plus, minus, multi-1, divide)
    
    if divide:
        dfs(depth + 1, int(num_sum/num_li[depth]), plus, minus, multi, divide-1)

num_sum = num_li[0]
dfs(1, num_sum,  operator[0], operator[1], operator[2], operator[3])

print(max_value)
print(min_value)