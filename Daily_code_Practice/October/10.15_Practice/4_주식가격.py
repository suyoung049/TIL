from collections import deque

prices = [1, 2, 3, 2, 3]
answer = []
 
q = deque(prices)


while q:
    price = q.popleft()

    count = 0

    for num_ in q:
        count += 1

        if price > num_:
            break

    answer.append(count)

print(answer)