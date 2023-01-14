n = 437674
k = 3
result = 0
re_num = []

# 10진수에서 n진수 변환 가능(10진수까지)
def convert_iter(num, k):
    tmp = ''
    while num:
        tmp = str(num%k) + tmp
        num //= k
    return tmp

num_ = convert_iter(n,k)
num_ =  num_.split('0')

for i in num_:
    if i == '':
        continue
    else:
        re_num.append(int(i)) 


for j in re_num:
    if j == 1:
        continue
    for k in range(2, int(j**0.5)+1):
        if j % k == 0:
            break
    else:
        result += 1

print(result)





