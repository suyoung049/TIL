N = int(input())
money = []
stack = []
for i in range(N):
    money.append(int(input()))

for num_ in money:
    if num_ != 0:
        stack.append(num_)
    else:
        stack.pop()
print(sum(stack))

        
