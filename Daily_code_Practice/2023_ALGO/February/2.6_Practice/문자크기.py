s = "Zbcdefg"
answer = []
resutl = ''


for i in s:
    answer.append(int(ord(i)))

answer.sort(reverse=True)

for j in answer:
    resutl += chr(j)

print(resutl)