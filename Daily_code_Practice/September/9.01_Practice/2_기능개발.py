progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1]
answer = []
time = 0
count = 0

while len(progresses)> 0:
    if (progresses[0] + time*speeds[0]) >= 100: 
        progresses.pop(0)
        speeds.pop(0)
        count += 1
        
    else:
        if count > 0:
            answer.append(count)
            count = 0
        time += 1
answer.append(count)
print(answer)