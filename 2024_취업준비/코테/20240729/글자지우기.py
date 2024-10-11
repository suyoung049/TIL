my_string , indices = "apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3]

def solution(my_string, indices):
    answer = ''
    sort_indices = sorted(indices)
    for idx in range(len(my_string)):
        if idx in indices:
            continue
        else:
            answer += my_string[idx]
    print(answer)

solution(my_string, indices)