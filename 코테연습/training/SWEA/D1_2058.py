num = input()
n = int(num)
sum = 0
i = 0
while n > 0:
    i = n % 10 
    n //= 10   
     
    sum += i
print(sum)