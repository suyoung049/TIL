dartResult = '1D2S#10S'
stack = []
dartResult = dartResult.replace('10', 'A')
score = {'S':1, 'D':2, 'T':3}

for i in dartResult:
    if i.isdigit():
        stack.append(int(i))
    elif i == 'A':
        stack.append(10)

    elif i in ('S','D','T'):
        num = stack.pop()
        stack.append(num**score[i])
    elif i == '#':
        num = stack.pop()
        stack.append(num*-1)
    elif i == '*':
        num = stack.pop()
        if stack:
            stack[-1] *= 2
        stack.append(num * 2)

print(stack)