arr =   [[1, 1], [1, 1], [1, 1], [1, 1]]

def solution(arr):
    y_len = len(arr)
    x_len = len(arr[0])

    # 열이 더 많은 경우
    if y_len > x_len:
        for lis in arr:
            for _ in range(y_len - x_len):
                lis.append(0)
    else:
        for _ in range(x_len - y_len):
            arr.append([0 for _ in range(x_len)])
    
    return arr

solution(arr)