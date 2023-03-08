N = 5 
K = 3

A = [1, 2, 5, 4, 3]
B = [5, 5, 6, 6, 5]

A.sort()
B.sort(reverse=True)

count_ = 0
for i in range(N):
    if A[i] < B[i]:
        A[i] = B[i]
        count_ += 1
        if count_ == K:
            break

print(sum(A))
    