word = "HappyHacking"

count = 0

for char in word:
    if char in ["a", "e", "i", "o" , "u"]: # '==' 표시가 아니라 in 으로 변경해주고
        count += 1                         # or을 제거해야 한다.

print(count)