str1 = 'A+C'
str2 = 'DEF'
str1 = str1.lower()
str2 = str2.lower()
answer = 0

dic_1 = []
dic_2 = []

for i in range(len(str1)-1):
    chr = str1[i] + str1[i+1]
    if chr.isalpha():
        dic_1.append(chr)
    
for i in range(len(str2)-1):
    chr = str2[i] + str2[i+1]
    if chr.isalpha():
        dic_2.append(chr)


a_temp = dic_1.copy()
uni = dic_1.copy()

for i in dic_2:
    if i not in a_temp:
        uni.append(i)
    else:
        a_temp.remove(i)
inter = []

for i in dic_2:
    if i in dic_1:
        dic_1.remove(i)
        inter.append(i)

inter = len(inter)
uni = len(uni)

if uni == 0:
    answer = 1 *65536

else:
    answer = int(65536 * (inter/uni))

print(answer)