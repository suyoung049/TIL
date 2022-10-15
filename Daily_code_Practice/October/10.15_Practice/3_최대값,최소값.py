s = "1 2 3 4"

arr = list(map(int, s.split(' ')))

answer = [str(min(arr)), str(max(arr))]

print(' '.join(answer))