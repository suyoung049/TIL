arry = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def insertion_sort(x):
    for r in range(len(x)-1):
        key = x[r+1]
        for i in range(r+1):
            if key < x[i]:
                x[i+1:r+2]=x[i:r+1] # 한 칸씩 미루기
                x[i] = key
                break
    return x


def shell_sort(x):
    n = len(x)
    gap = n//2
    while gap >= 1:
        for s in range(gap):
            t = x[s:n:gap]
            insertion_sort(t)
        gap = gap//2

shell_sort(arry)


