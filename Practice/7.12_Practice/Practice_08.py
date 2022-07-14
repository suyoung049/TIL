num = [0, 20, 100, 40, 60]
max_num = 0
second_num = 0
for n in num:
    if max_num < n: # 만약에, n이 최대보다 크다면
        second_num = max_num
        max_num = n
    elif second_num < n and n < max_num:
        second_num = n
print(second_num)


