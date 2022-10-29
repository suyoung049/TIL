A = [1, 4, 2]
B = [5, 4, 4]

A.sort()
B.sort(reverse=True)

sum_ = 0
for i in range(len(A)):
    sum_ += A[i] * B[i]

print(sum_)
