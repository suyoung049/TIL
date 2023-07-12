def solution(s):
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    answer = s
    for key in num_dic:
        answer = answer.replace(key,num_dic[key])
    
    return int(answer)