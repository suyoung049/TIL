k = 2
d = 4

result = 0

for i in range(0, d+1 ,k):
    j = (d*d) - (i*i)
    j = (int(j **(0.5))//k) +1
    print(j)
    result += j
print(result)

x = []
for i in range(0, d+1 ,k):
    j = (d*d) - (i*i)
    j = int(j **(0.5))
    for y in range(0 , j+1, k):
        x.append(y)
print(len(x))


    