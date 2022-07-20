n = int(input())
a = map(int, input().split())
min = 100000
for i in a:
    if i < min:
        min = i
print(min)