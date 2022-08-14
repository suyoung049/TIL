n = 0
word = input()
# 모든 문자를 돌려서
for i in word:
    n += 1 # n = n+1
    # 1씩 증가시킨다
print(n)

while(n < len(word)):
    n += 1
print(n)