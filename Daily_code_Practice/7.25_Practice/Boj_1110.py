n = int(input())
re_N = n
count = 0
while True:
    a = re_N // 10
    b = re_N % 10
    c = (a + b) % 10
    re_N = (b * 10 + c)
    count += 1
    if re_N == n:
        break
print(count)
    