import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

sequence = [num_list[0]]


for i in range(len(num_list)):
    if sequence[-1] < num_list[i]:
        sequence.append(num_list[i])

    
    else:
        start = 0
        end = len(sequence) - 1

        while True:
            if start > end:
                break

            mid = (start + end) //2

            if sequence[mid] < num_list[i]:
                start = mid + 1
                
            else:
                end = mid - 1
    

        sequence[start] = num_list[i]

print(len(sequence))