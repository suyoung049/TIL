import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

book_location = list(map(int, input().split()))

right_location = []
left_location = []

max_length = 0
for location in book_location:
    max_length = max(max_length, abs(location))
    if location < 0:
        left_location.append(location)
    else:
        right_location.append(location)


sort_right = sorted(right_location, reverse=True)
sort_left = sorted(left_location)
print(sort_right)
print(sort_left)

result = 0
for i in range(0, len(sort_right), m):
    result += sort_right[i]*2
for i in range(0, len(sort_left), m):
    result += abs(sort_left[i])*2

print(result - max_length)
