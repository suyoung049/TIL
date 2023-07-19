k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]

result = 0

score.sort()

while True:
    box = []
    for _ in range(m):
        apple = score.pop()
        box.append(apple)
    
    result += min(box) * m

    if len(score) < m or len(score) == 0:
        break

print(result)