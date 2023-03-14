import sys
sys.stdin = open('1_input.txt', 'r')
input = sys.stdin.readline

while True:
    histogram = list(map(int, input().split()))

    if histogram[0] == 0:
        break
    
    len_histogram = histogram.pop(0)
    
    stack = []
    max_histo = 0
    for i in range(len_histogram):
        if i == 0:
            stack.append((i,histogram[i]))

        else:
            while True:
                if stack[-1][1] > histogram[i]:
                    idx = stack.pop()

                    if not stack:
                        max_histo = max(max_histo, i * idx[1])
                        stack.append((i,histogram[i]))
                        break

                    else:
                        max_histo = max(max_histo, ((i-stack[-1][0]-1) * idx[1]))
                
                else:
                    stack.append((i, histogram[i]))
                    break

    if stack:
        while True:
            if len(stack) == 1:
                idx = stack.pop()
                max_histo = max(max_histo, len_histogram * idx[1])
                break

            
            else:
                idx = stack.pop()
                max_histo = max(max_histo, ((len_histogram-stack[-1][0]-1) * idx[1]))

    print(max_histo)

