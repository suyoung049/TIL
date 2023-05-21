import sys
sys.stdin = open("1_input.txt", "r")

text = input()

re_text = text[::-1]

if text == re_text:
    print(1)

else:
    print(0)