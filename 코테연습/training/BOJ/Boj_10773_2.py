stack = []

for _ in range(int(input())):
    num_ = int(input())

    if num_ == 0:
        stack.pop()
    else:
        stack.append(num_)

print(stack)