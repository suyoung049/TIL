n = int(input())
sum = 0
for i in range(0, 1000):
    if sum >= n:
        print(i-1)
        break
    sum += i

num = int(input())

s = 0
t = 0
while s<n :
  t += 1
  s += t
  
print(t)
  
    
