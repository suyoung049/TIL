import sys
sys.stdin = open("1_input.txt", "r")

word = input()

len_ = len(word)
result = []

for i in range(len_):
    parsing = word[i:len_]
    result.append(parsing)

result = sorted(result)

for i in range(len_):
    print(result[i])