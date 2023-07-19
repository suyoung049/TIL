from collections import Counter

X = "5525"
Y = "1255"

couple = []

x_count = Counter(X)
y_count = Counter(Y)

for x_chr in x_count:
    
    if x_chr in y_count:
        chr_cnt = min(x_count[x_chr], y_count[x_chr])

        for _ in range(chr_cnt):
            couple.append(x_chr)

check = True
if not couple:
    print("-1")


for test_chr in couple:
    if test_chr != "0":
        check = False


if check == False:
    couple.sort(reverse=True)
    print("".join(couple))

elif couple and check == True:
    print("0")