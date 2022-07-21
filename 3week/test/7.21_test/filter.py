numbers = [1, 2, 5, 19, 3, 9, 12]
result = []
for num in numbers:
    if num % 3 == 0:
        result.append(num)
print(result)

print(list(filter(lambda n: n%3==0, numbers)))