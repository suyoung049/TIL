import sys

sys.stdin = open("14_나머지.txt")

num_list = []
senum = set()

for _ in range(10):
    num_list.append(int(input())) # [0,1,2]
    

for i in range(len(num_list)):
    senum.add(num_list[i]% 42)  
print(len(senum))
