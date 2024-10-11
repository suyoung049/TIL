queue1 = [1, 1]
queue2 = [1, 5]

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    if (sum1 + sum2) % 2 == 1:
        return -1
    length = len(queue1)
    l1, r1 = 0, length-1
    l2, r2 = length, length*2 - 1
    n = 0
    while sum1 != sum2:
        if l2 >= (length * 2):
            n = -1
            break
        if sum1 > sum2:
            cnt = getNum(l1, length, queue1, queue2)
            sum1 -= cnt
            sum2 += cnt
            l1 += 1
            r2 += 1
            n += 1
        else:
            cnt = getNum(l2, length, queue1, queue2)
            sum1 += cnt
            sum2 -= cnt
            r1 += 1
            l2 += 1
            n += 1
    return n

def getNum(num, length, queue1, queue2):
    if num < length:
        result = queue1[num]
    else:
        result = queue2[num - length]
    return result


print(solution(queue1, queue2))