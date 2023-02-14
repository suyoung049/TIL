n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
stack = []
m = len(words)
a, b, = 0, 0


for i in range(1, m):
    if words[i-1] in stack:
        a = (i//n) + 1
        b = (i) % n

        if b == 0:
            b = n
        break

    elif words[i-1][-1] == words[i][0]:
        stack.append(words[i-1])
    
    else:
        a = (i//n) + 1
        b = (i+1) % n

        if b == 0:
            b = n
        break

if (a,b) == (0,0):

    if words[-1] in stack:
        a = ((m-1)//n)  + 1
        b = m % n

        if b == 0:
            b = n

print([b,a])



        