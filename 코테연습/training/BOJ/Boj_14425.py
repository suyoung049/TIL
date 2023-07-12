import sys

sys.stdin = open("14425_input.txt", "r") 
input = sys.stdin.readline
N, M = map(int, input().split())
s = []
words = []
for i in range(N):
    s.append(input())
for j in range(M):
    words.append(input())
word_set = set(words)
s_set = set(s)
cnt = 0
for word in word_set:
    if word in s:
        cnt += 1
print(cnt)
print(len(word_set & s_set))



