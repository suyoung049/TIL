n = 4
def solution(n):
    convert_li = convert(n)

    for i in range(len(convert_li) - 1, 0, -1):
        if  convert_li[i] == 0:
            convert_li[i] = 4
            convert_li[i-1] = (convert_li[i-1]) - 1
        elif convert_li[i] == -1:
            convert_li[i] = 2
            convert_li[i-1] = (convert_li[i-1]) - 1

    for i in range(len(convert_li)):
        if (convert_li[i]) > 0 :
            convert_li = convert_li[i:]
            break
    
    for i in range(len(convert_li)):
        convert_li[i] = str(convert_li[i])
    
   
    return "".join(convert_li)

def convert(n):
    convert_num = []
    
    while n > 0:
        convert_num.append((n%3))
        n = n //3

    return convert_num[::-1]


print(solution(n))