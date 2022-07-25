N, x = map(int, input().split())
numbers = map(int, input().split())

for number in numbers:
    if number >= x:
        continue
    print(number, end = ' ') 
