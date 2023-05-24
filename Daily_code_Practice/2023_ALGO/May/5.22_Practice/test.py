from collections import deque
def solution(babbling):
    speak = ["aya", "ye", "woo", "ma"]
    stack = ''
    answer = 0

    for chr_ in babbling:
        chr_ = deque(chr_)
        temp = ["a"]
        while True:
            c = chr_.popleft()
            stack += c
            if stack in speak:
                if temp[-1] == stack:
                    stack = ''
                    break
                else:
                    temp.append(stack)
                    stack = ''

            if len(chr_) == 0:
                if stack == '':
                    answer += 1
                    break
                else:
                    stack = ''
                    break
    return answer
