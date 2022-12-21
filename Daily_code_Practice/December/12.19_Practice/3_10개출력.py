import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

a = input()
i = 0

while True:
    
    if (i+1)*10 > len(a):
        print(a[i*10:len(a)])
        break
    else:
        print(a[i*10:(i+1)*10])
    
    i += 1



