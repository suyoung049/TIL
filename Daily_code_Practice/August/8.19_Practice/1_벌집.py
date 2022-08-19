import sys
sys.stdin = open('1_input.txt', 'r')

N = int(input())
line = 1
last_num = 1
if N == 1:
    print(1)
else:
    while True:
        if N <= last_num:
            print(line)
            break

        last_num += (6 * line)
        line += 1