import sys
sys.stdin = open('2_input.txt', 'r')
input = sys.stdin.readline

n, r, c = map(int, input().split())

def z(n, r, c, q):
    
    half = 2 ** (n-1)

    if n == 0:
        print(q)
        return 
    
    else:
        if r < half:
            if c < half:
                quard = 1
            else:
                quard = 2
                c -= half
        else:
            if c < half:
                quard = 3
                r -= half
            else:
                quard = 4
                r-= half
                c-= half            
    
    q += (quard - 1) * (half ** 2)
    z(n-1, r, c, q)

z(n, r, c, 0)