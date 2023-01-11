quiz = ["3 - 4 = -3", "5 + 6 = 11"]
result = []

for i in  quiz:
    i = i.split('=')
    if eval(i[0]) == int(i[1]):
        result.append('O')
    
    else:
        result.append('X')

print(result)