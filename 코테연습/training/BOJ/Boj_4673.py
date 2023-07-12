for N in range(1, 101):
    num_list = []
    de_sum = 0
    for i in range(1, N):
        num_ = list(map(int, str(i)))
        de_sum = i + sum(num_)
        if de_sum == N:
            num_list.append(i)
    if len(num_list) == 0:
        print(N)
            