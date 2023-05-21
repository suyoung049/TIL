import sys
sys.stdin = open("3_input.txt", "r")


word = input()

len_ = len(word)

result = set()

for j in range(len_-1):
    for i in range(len_):
        result.add(word[i:i+j+1])
result.add(word)
print(len(result))