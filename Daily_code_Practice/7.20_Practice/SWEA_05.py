a = input()
n = int(a)
n < 30
x = 1
i = 0

for i in range(0, n+1):
    y = x * (2**i)
    i += 1
    print(y, end = ' ')
   
