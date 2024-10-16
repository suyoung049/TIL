from collections import deque

s = "()()"

def solution(s):
    answer = True
    s_list = deque([])
    stack = []

    for syn in s:
        s_list.append(syn)

    while s_list:
        sign = s_list.popleft()
        if sign == '(':
            stack.append(sign)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            
            else:
                stack.append(sign)
    
    if stack:
        answer = False

    return answer

solution(s)