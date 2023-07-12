N = int(input())
coun = 0

for i in range(1, N+1):
    if i < 100:
        coun += 1

    else:
        num_ = list(map(int, str(i))) # 각자리가 등차수열이므로 수 를 각각 변환
        if num_[0] - num_[1] == num_[1] - num_[2]: # 각 자리가 등차수열
            coun += 1
print(coun)