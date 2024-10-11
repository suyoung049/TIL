bin1, bin2 = "1111111111", 	"1111111111"

def solution(bin1, bin2):
    answer = ''
    digit = []
    length = len(bin1)
    if len(bin1) != len(bin2):
        if len(bin1) > len(bin2):
            n = len(bin1) - len(bin2)
            bin2 = meta(bin2, n)
        else:
            n = len(bin2) - len(bin1)
            length = len(bin2)
            bin1 = meta(bin1, n)

    for i in range(length-1, -1, -1):
        if bin1[i] == "1":
            digit.append("1")
        
        if bin2[i] == "1":
            digit.append("1")
        
        if len(digit) == 3:
            answer += "1"
            digit = ["1"]
        
        elif len(digit) == 2:
            answer += "0"
            digit = ["1"]
        
        elif len(digit) == 1:
            answer += "1"
            digit = []
        elif len(digit) == 0:
            answer += "0"
            digit = []
      
    if len(digit):
        answer += "1"
    
    
    return answer[::-1]


def meta(a, n):
    str_num = ""
    for i in range(n):
        str_num += "0"
    
    str_num += a

    return str_num


solution(bin1, bin2)