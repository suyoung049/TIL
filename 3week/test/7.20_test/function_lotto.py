import random

def generate_lotto(n):
    result = []
    for i in range(n):
        num = range(1, 46)
        pick = random.sample(num, 6)
        pick.sort()
        result.append(pick)
    return result

print(generate_lotto(5))
