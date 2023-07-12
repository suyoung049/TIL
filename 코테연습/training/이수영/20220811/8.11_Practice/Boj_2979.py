import sys

sys.stdin = open("2979_input.txt", "r")

a, b, c = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

truck_1 = set()
truck_2 = set()
truck_3 = set()
for i in range(x1, y1):
    truck_1.add(i)
for j in range(x2, y2):
    truck_2.add(j)
for k in range(x3, y3):
    truck_3.add(k)
p_3 = (truck_1 & truck_2 & truck_3)
p_2 = ((truck_1 & truck_2) | (truck_1 & truck_3)) - p_3 
p_1 = (truck_1 | truck_2 | truck_3) -p_3 -p_2
price = (len(p_3) * (c*3)) + (len(p_2) * (b*2)) + (len(p_1) * a) 
print(price)
print(p_3)
print(p_2)
print(p_1)