import sys
sys.stdin = open('6_input.txt', 'r')
input = sys.stdin.readline

a, b, c = map(int, input().split())


def fastpower(a,b,c):
    if b == 0:
        return 1 % c
  
    
    else:
        tmp = fastpower(a, b//2, c) 
        if b % 2 == 0:
            return (tmp * tmp) % c
    
        else:
            return (tmp * tmp * a) % c

print(fastpower(a,b,c))

