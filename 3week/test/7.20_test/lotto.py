import random

for i in range(5):
    num = range(1, 46)
    result = random.sample(num, 6)
    result.sort()

    print(result)