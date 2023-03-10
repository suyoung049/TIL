nums = [9,7,5,3,1]
import heapq

heapq.heapify(nums)


# 3번째로 작은 수 찾기

heapq.heappop(nums)
print(nums)

heapq.heappop(nums)
print(nums)

print(nums[0])