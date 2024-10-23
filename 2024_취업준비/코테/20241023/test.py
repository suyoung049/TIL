def check_num(num):
    check = []
    for k in range(1, int(num**0.5) + 1):
        if num % k == 0:
            check.append(k)
            check.append(num//k)
    if len(check) == 2:
        return True
    else:
        return False
    
check_num(1)