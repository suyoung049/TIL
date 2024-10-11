code = "abc1abc1abc"
def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i] == "1":
                print("modeChange")
                mode = 1
            else:
                if (i % 2 == 0):
                    print(i, 'mode==0')
                    answer += code[i]
        else:
            if code[i] == "1":
                mode = 0
            else:
                if (i % 2 != 0):
                    print(i, "mode==1")
                    answer += code[i]
                          
    return answer


solution(code)