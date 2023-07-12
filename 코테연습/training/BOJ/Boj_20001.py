import sys

sys.stdin = open("20001_input.txt", "r", encoding = 'UTF-8')

stack = []
text = input()

while True:
    s = input()
    if s == '문제':
        stack.append(1)
    if s == '고무오리':
        if not stack:
            stack.append(1)
            stack.append(1)
        else:
            stack.pop()
    if s == '고무오리 디버깅 끝':
        break
if not stack:
    print('고무오리야 사랑해')
else:
    print('힝구')