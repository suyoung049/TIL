c = ord(input()) # 순서대로 표기하기 위해서 ord 치한?
t = ord('a') # 초기값
while t<=c:      # a부터 입력한 문자까지
    print(chr(t), end = ' ')
    t += 1