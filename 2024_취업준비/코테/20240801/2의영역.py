arr = [1, 2, 1, 4, 5, 2, 9]

def solution(arr):
    answer = []
    index_li = []
    idx = 0
    for num in arr:
        idx += 1
        if (num == 2):
            index_li.append(idx-1)
    print(index_li)
    if not index_li:
        answer = [-1]
    else:
        answer = arr[index_li[0]:index_li[-1] + 1 ]
    return answer

solution(arr)