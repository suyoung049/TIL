import copy
arr = [1, 2, 3, 100, 99, 98]

def solution(arr):
    count = 0
    while True:
        origin_arr = copy.deepcopy(arr)
        change_arr = change_list(arr)

        if same_list(change_arr, origin_arr):
            break
        else:
            count += 1
            arr = change_arr
 
       
def change_list(arr):
    for i in range(len(arr)):
        if (arr[i] % 2 == 0):
            if ( 50 <= arr[i]):
                arr[i] = arr[i]//2
        else:
            if ( 50 > arr[i]):
                arr[i] = (arr[i] * 2)  + 1
    return arr


def same_list(a, b):
    plage = True
    for i in range(len(a)):
        if (a[i] != b[i]):
            plage = False

    return plage

solution(arr)