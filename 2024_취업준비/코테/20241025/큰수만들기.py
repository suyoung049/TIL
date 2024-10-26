number = "10"
k = 1

def solution(number, k):
    answer = ''
    stack = []
    cnt = 0
    for num in number:
        while True:
            if cnt == k:
                stack.append(num)
                break
            if not stack:
                stack.append(num)
                break
            last = int(stack[-1])
            if last < int(num):
                stack.pop()
                cnt += 1
            else:
                stack.append(num)
                break
    if k != cnt:
        for _ in range(k-cnt):
            stack.pop()  
            
    for st_num in stack:
        answer += st_num
    return answer


print(solution(number, k))