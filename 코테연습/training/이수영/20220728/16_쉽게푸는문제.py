a,b = map(int, input().split())
num_list = []
sum = 0
for i in range(1, b+1):
    for j in range(i):
        num_list.append(i)
num_list = list(map(int, num_list))
print(num_list)
for k in range(a-1,b):
    sum += num_list[k]
print(sum)