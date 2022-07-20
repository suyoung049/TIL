num = input()
n = int(num)
sum = 0
i = 0
while n > 0:
    i = n % 10 
    n //= 10   
    print(int(i, end =''))

# number = 123
# print(int(str(number)[::-1]))

num = 123
result = 0
while num:
    result *= 10
    result += num%10
print(result)