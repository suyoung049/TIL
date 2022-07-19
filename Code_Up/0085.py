w, h, b = (map(int, input().split()))

result = float((w * h * b)/(8*1024*1024))
print(format(result, '.2f'), 'MB')