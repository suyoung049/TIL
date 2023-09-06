import sys
sys.stdin = open('1_input.txt')

n, k = map(int, input().split())

ice_li = [0] * 1000001
max_location = 0
for _ in range(n):
    weight, locaion = map(int, input().split())
    ice_li[locaion] = weight
    max_location = max(max_location, locaion)

ice_range = (2 * k) + 1
ice_sum = sum(ice_li[:ice_range])
max_sum = ice_sum

for j in range(ice_range, max_location):
    ice_sum = ice_sum + ice_li[j] - ice_li[j-ice_range]
    max_sum = max(max_sum, ice_sum)

print(max_sum)