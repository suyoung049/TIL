import sys
sys.stdin = open("1_input.txt", "r")

text = input()



len_ = len(text)
result = ""

for i in range(len_):
    if str.isalpha(text[i]):
        if 97 <= ord(text[i]) < 110 or 65<= ord(text[i]) <= 77:
            result += chr(ord(text[i]) + 13)
        
        else:
            if 78<= ord(text[i]) < 91 or 110 <= ord(text[i]):
                result += chr(ord(text[i])-13)
    
    else:
        result += text[i]

print(result)