sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

hor = []
ver = []

for len in sizes:
    if len[0] >= len[1]:
        hor.append(len[0])
        ver.append(len[1])
    
    else:
        hor.append(len[1])
        ver.append(len[0])

print(max(hor) * max(ver))