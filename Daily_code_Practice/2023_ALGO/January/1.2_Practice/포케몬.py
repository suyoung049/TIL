

N,M = map(int, input().split())


animal = ['sample']
for i in range(N):
    data = input()
    animal.append(data)

for j in range(M):
    data = input()
    try:
        data = int(data)
        print(animal[data])
    except:
        for i in range(len(animal)):
            if animal[i] == data:
                print(i)
