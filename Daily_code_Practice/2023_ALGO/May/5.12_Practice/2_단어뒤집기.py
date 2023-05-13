import sys
sys.stdin = open("2_input.txt", "r")

text = input()
check = False

word = ""

len_ = len(text)

for i in range(len_):
    if text[i] == ">":
        check = False
        word += text[i]
        print(word, end="")
        word = ""
    
    elif text[i] == '<':
        check = True
        if i != 0:
            print(word[::-1], end="")
            word = ""
            word += text[i]
        elif i == 0:
            word += text[i]
    elif text[i] == " ":
        if check == False:
            print(word[::-1], end=" ")
            word = ""
        else:
            word += text[i]
    
    else:
        word += text[i]

if len(word) != 0:
    print(word[::-1])


        

    


