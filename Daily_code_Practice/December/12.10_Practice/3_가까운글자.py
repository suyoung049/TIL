s = "foobar"

stack = []
answer = []


for i in range(len(s)):
    num_list = []
    if s[i] not in stack:
        answer.append(-1)
        stack.append(s[i])
    else:
        for j in range(len(stack)):
            if stack[j] == s[i]:
                num_ = i - j
                num_list.append(num_)
        answer.append(min(num_list))
        stack.append(s[i])

print(answer)
                
                


    
  

    