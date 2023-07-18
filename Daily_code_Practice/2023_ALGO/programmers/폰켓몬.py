nums = [3,1,2,3]

half_length = (len(nums)//2)

set_nums = set(nums)

if half_length <= len(set_nums):
    print(half_length)
else:
    print(set_nums)