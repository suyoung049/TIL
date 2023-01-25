fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

# box = {}

# for i in fruits:
#     if i in box:
#         box[i] += 1

#     else:
#         box[i] = 1


# def fru(i):
#     print(box[i])

# fru('사과')

def co_fru(i):
    coun = 0

    for fruit in fruits:
        if fruit == i:
            coun += 1
    
    return coun

print(co_fru('배'))