input = (str(['92', '93']))

orderlists = []
temp = ''
for i in range(len(input)):
 
    
    if input[i] != ',' and input[i] != '\'' and input[i] != '[' and input[i] != ']':
        temp += input[i]
    
    if input[i] == ',' or input[i] ==  ']':
        orderlists.append(temp)
        temp = ''
orderlist = list(map(int, orderlists))

for i in orderlist:
    print(i, type(i))