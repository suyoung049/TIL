import sys

sys.stdin = open("1076_input.txt", "r")

gap = {
    'black' : 0,
    'brown' : 1,
    'red' : 2,
    'orange' : 3,
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9 
}
color = []
for _ in range(3):
    color.append(input())
for i in range(len(color)-2):
    resi = int(str(gap[color[i]]) + str(gap[color[i+1]])) * (10 ** gap[color[i+2]])
print(resi)

