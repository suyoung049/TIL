from collections import deque
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2

num_list = deque(num_list)
result = []

count_ = len(num_list)//n

for y in range(count_):
    stack = []
    for x in range(n):
        i = num_list.popleft()
        stack.append(i)
    result.append(stack)

print(result)
