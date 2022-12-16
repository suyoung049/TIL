a = [1,2,3,4]
b = [-3,-1,0,2]

num_list = []

for i in range(len(a)):
    sum_ = a[i] * b[i]
    num_list.append(sum_)

print(sum(num_list))
