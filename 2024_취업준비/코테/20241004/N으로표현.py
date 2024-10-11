N, number = 5, 12
def solution(N, number):
    # i개의 N으로 만들수 있는 리스트 담겨 있는 딕셔너리
    check, num_dict = set(), dict()
    for i in range(1, 9):
        list_num = int(str(N) * i)
        if list_num == number:
            return i
        else:
            num_dict[i] = [list_num]
            check.add(list_num) 
    
    # 2개 만드는데 (1, 1)
    # 3개 만드는 (1, 2), (2, 1)
    # 4개 만드는데 (1, 3), (2, 2), (3, 1)
    # 5개 만드는데 (1, 4), (2, 3), (3, 2), (4, 1)
    for i in range(2, 9):
        test_list = []
        for j in range(1, i):
             if j in test_list:
                 continue
             k = i -j
             test_list.append(k)
             for num_j in num_dict[j]:
                 for num_k in num_dict[k]:
                     candidates = [num_j + num_k, abs(num_j - num_k), num_k//num_j, num_j//num_k, num_j * num_k]
                     for candidate in candidates:
                         if candidate < 1:
                             continue
                         
                         if candidate in check:
                             continue
                         
                         if candidate == number:
                             return i
                         
                         num_dict[i].append(candidate)
                         check.add(candidate)

    return -1

print(solution(N, number))