import sys

sys.stdin = open("1181_input.txt", "r")

N = int(input())
word_list = []
for _ in range(N):
    word_list.append(input())

word_list = set(word_list)
w_list_1 = sorted(word_list)
w_list_2 = sorted(w_list_1, key = len)

for word in w_list_2:
    print(word)
