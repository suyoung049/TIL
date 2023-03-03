import sys
sys.stdin = open('4_input.txt', 'r')

score = int(input())


if score < 60:
    print('E')
elif 60 <= score < 70:
    print('D')
elif 70<= score < 80:
    print('C')
elif 80<= score < 90:
    print('B')
else:
    print('A')