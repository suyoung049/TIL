import sys

sys.stdin = open("1264_input.txt", "r")
word = ['a', 'e', 'i', 'o', 'u']

while True:
    text = input()
    if text == '#':
        break
    else:
        coun = 0
        text_l = text.lower()
        for i in range(len(text_l)):
            if text_l[i] in word:
                coun += 1
        print(coun)
    



