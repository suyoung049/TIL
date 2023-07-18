dirs ="RRRRRDLDRDLDRDLURULURULUR"

check = set()
answer = 0
y, x = 0, 0

length = len(dirs)

for i in range(length):
    if dirs[i] == "U":
        ny = y + 1
        nx = x
        if -5<= ny <= 5:
            go = (y, x, ny, nx)
            back = (ny, nx, y, x)
            
            y = ny 
            x = nx

            if go not in check:
                check.add(go)
                check.add(back)
                answer += 1
      
    
    elif dirs[i] == "D":
        ny = y - 1
        nx = x
        if -5<= ny <= 5:
            go = (y, x, ny, nx)
            back = (ny, nx, y, x)
            
            y = ny 
            x = nx

            if go not in check:
                check.add(go)
                check.add(back)
                answer += 1
    
    
    elif dirs[i] == "R":
        ny = y 
        nx = x + 1
        if -5<= nx <= 5:
            go = (y, x, ny, nx)
            back = (ny, nx, y, x)
            
            y = ny 
            x = nx

            if go not in check:
                check.add(go)
                check.add(back)
                answer += 1

    else:
        ny = y 
        nx = x - 1
        if -5<= nx <= 5:
            go = (y, x, ny, nx)
            back = (ny, nx, y, x)
            y = ny 
            x = nx

            if go not in check:
                check.add(go)
                check.add(back)
                answer += 1
        

print(answer)