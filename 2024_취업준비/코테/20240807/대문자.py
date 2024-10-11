myString = "aBcDeFg"

def solution(myString):
    answer = ''
    for str in myString:
        if (str.isupper()):
            answer += str
        else:
            print(str.upper())
            answer +=  str.upper()
    print(answer)
    return myString

solution(myString)