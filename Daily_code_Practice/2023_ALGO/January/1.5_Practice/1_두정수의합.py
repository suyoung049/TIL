a, b = 3, 5

result = 0

if a > b:
    for i in range(b, a+1):
        result += i

else:
    for i in range(a, b+1):
        result += i 

print(result)