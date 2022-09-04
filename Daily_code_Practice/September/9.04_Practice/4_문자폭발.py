import sys
sys.stdin = open('4_input.txt', 'r')

text = input()

bomb = list(input())

stack = []   # bomb의 글자열을 없애줄 stack


for chr in text:
    stack.append(chr) # text 문자열을 stack에 저장해준다.

    if len(stack) >= len(bomb): # 폭탄문자의 길이보다 길어지면 폭탄을 제거 할수 있다.
        
        if stack[-len(bomb):] == bomb:  # stack의 마지막 글자가 폭탄가 같아지면

            for _ in range(len(bomb)):
                stack.pop()                   # 폭탄의 수만큼 제거 

if stack:
    for chr in stack:
        print(chr, end ='')
else:
    print('FRULA')




