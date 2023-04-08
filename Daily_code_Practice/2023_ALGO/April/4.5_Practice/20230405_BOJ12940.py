import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline


s = input().strip()
t = input().strip()


def reverse(chr):
    reverse_t = ''
    for i in range(len(chr)-1, -1, -1):
        reverse_t += chr[i]
    
    return reverse_t


while True:

    if t[-1] == 'A':
        t = t[:-1]
    
    else:
        t = t[:-1]
        t = reverse(t)
    
    
    if len(t) == len(s):
        if t == s:
            print(1)
        else:
            print(0)
        
        break
    

