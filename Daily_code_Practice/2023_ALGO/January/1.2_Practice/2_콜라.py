a, b, n = 2, 1, 20

answer = 0

while True:
    co = (n//a) * b
    co_1 = n%a
    answer += co
    n = co + co_1

    if n < a:
        break

print(answer)
    