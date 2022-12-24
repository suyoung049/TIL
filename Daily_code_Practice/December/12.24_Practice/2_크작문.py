t = "10203"
p = "15"

length = len(p)
count = 0

for i in range((len(t)+1)-length):
    num = t[i:i+length]

    if int(num) <= int(p):
        count += 1

print(count)
    