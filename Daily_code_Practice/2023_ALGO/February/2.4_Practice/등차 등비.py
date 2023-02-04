common = [2, 4, 8]
check = True

if common[1] - common[0] == common[2] - common[1]:
    check = False


if check == False:
    result = common[-1] + (common[1]-common[0])

else:
    result = common[-1] * (common[1]//common[0])

print(result)