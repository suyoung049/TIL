n= 5
for i in range(1, n+1): #1~2n
    print('*' * i + ' ' * (n - i) + ' ' * (n - i) + '*' * i)
for i in range(n-1, 0, -1): # n-1 ~ 1
    print('*' * i + ' ' * (n - i) + ' ' * (n - i) + '*' * i)