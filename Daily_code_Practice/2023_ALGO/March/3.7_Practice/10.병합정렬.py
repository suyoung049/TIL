import sys
sys.stdin = open('3_input.txt', 'r')
input = sys.stdin.readline

n = int(input())   


a = []

for _ in range(n):
    a.append(int(input()))

def _merge_sort(a, left, right):
    if left < right:
        center = (left + right) // 2
        
        _merge_sort(a, left, center)
        _merge_sort(a, center + 1, right)

        p = j = 0
        i = k = left

        while i <= center:
            buff[p] = a[i]
            p += 1
            i += 1

        while i <= right and j < p:
            if buff[j] <= a[i]:
                a[k] = buff[j]
                j += 1
            else:
                a[k] = a[i]
                i += 1
            k += 1

        while j < p:
            a[k] = buff[j]
            k += 1
            j += 1

n = len(a)
buff = [0] * n
_merge_sort(a, 0, n-1)
del buff

print(a)

