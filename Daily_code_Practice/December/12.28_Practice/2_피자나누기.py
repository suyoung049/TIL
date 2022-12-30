n = 6
pizza = 6
order = []


for i in range(max(n, pizza), (n * pizza) + 1):
    if i % n == 0 and i % pizza == 0:
        order.append(i)
        
order = min(order)

answer = order//6

print(answer)