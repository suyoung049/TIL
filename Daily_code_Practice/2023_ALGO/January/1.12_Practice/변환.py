arr = 123
arr = str(123)
sum_ = 0

for i in range(len(arr)):
    n = int(arr[i])
    sum_ += n

if int(arr) % sum_ == 0:
    answer = 'true'

else:
    answer = 'false'

print(answer)
    