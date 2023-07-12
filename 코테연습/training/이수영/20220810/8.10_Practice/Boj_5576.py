import sys

sys.stdin = open("5576_input.txt", "r")

w_score = []
k_score = []

for _ in range(10):
    w_score.append(int(input()))

for _ in range(10):
    k_score.append(int(input()))

best_score_w = sorted(w_score, reverse = True)
best_score_k = sorted(k_score, reverse = True)
print(sum(best_score_w[:3]), sum(best_score_k[:3]))
