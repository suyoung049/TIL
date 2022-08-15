num = input()
n = int(num)
sum = 0
i = 0
while n > 0:
    i = n % 10 
    n //= 10   
    print(i, end ='')

# number = 123
# print(int(str(number)[::-1]))
