
m = 'cdcd'
stack = []

for i in m:
    if len(stack) == 0:
        stack.append(i)
    elif stack[-1] == i:
        stack.pop()
    
    else:
        stack.append(i)

print(stack)
if len(stack) == 0:
    print(1)
else:
    print(0)
