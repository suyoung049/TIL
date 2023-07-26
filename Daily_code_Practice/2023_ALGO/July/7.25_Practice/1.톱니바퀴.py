import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

def pprint(list_):
    for row in list_:
        print(row)

def counterclockwise(pick_gear):
    gear_set = temp_gear[pick_gear]

    for i in range(8):
        if i == 7:
            gear_set[i] = gear[pick_gear][0]
        else:
            gear_set[i] = gear[pick_gear][i+1]

def clockwise(pick_gear):
    gear_set = temp_gear[pick_gear]

    for i in range(8):
        if i == 0:
            gear_set[i] = gear[pick_gear][7]
        else:
            gear_set[i] = gear[pick_gear][i-1]

temp_gear = [[0] * 8 for _ in range(4)]
gear = [list(map(int, input().strip())) for _ in range(4)]

rotation_num = int(input())
rotation_li = []

for _ in range(rotation_num):
    gear_num, rotation_direction = map(int, input().split())
    rotation_li.append((gear_num, rotation_direction))


for gear_num, rotation_direction in rotation_li:
    if gear_num == 1:
        gear_num = gear_num - 1
        
        if gear[gear_num][2] != gear[gear_num + 1][6]:
            if rotation_direction == -1:
                clockwise(gear_num + 1)
                gear[gear_num + 1] = temp_gear[gear_num + 1]
            
            else:
                counterclockwise(gear_num + 1)
                gear[gear_num + 1] = temp_gear[gear_num + 1]
        
        if rotation_direction == -1:
            counterclockwise(gear_num)
            gear[gear_num] = temp_gear[gear_num]
        else:
            clockwise(gear_num)
            gear[gear_num] = temp_gear[gear_num]
    
    elif gear_num == 2 or gear_num == 3:
        gear_num = gear_num - 1
        
        if gear[gear_num][2] != gear[gear_num + 1][6]:
            if rotation_direction == -1:
                clockwise(gear_num + 1)
                gear[gear_num + 1] = temp_gear[gear_num + 1]
            
            else:
                counterclockwise(gear_num + 1)
                gear[gear_num + 1] = temp_gear[gear_num + 1]
        
        if gear[gear_num][6] != gear[gear_num - 1][2]:
            if rotation_direction == -1:
                clockwise(gear_num - 1)
                gear[gear_num - 1] = temp_gear[gear_num - 1]
            
            else:
                counterclockwise(gear_num - 1)
                gear[gear_num - 1] = temp_gear[gear_num - 1]
        
        if rotation_direction == -1:
            counterclockwise(gear_num)
            gear[gear_num] = temp_gear[gear_num]
        else:
            clockwise(gear_num)
            gear[gear_num] = temp_gear[gear_num]

    elif gear_num == 4:
        gear_num = gear_num - 1
        
        if gear[gear_num][6] != gear[gear_num -1][2]:
            if rotation_direction == -1:
                clockwise(gear_num -1)
                gear[gear_num -1] = temp_gear[gear_num -1]
            
            else:
                counterclockwise(gear_num - 1)
                gear[gear_num - 1] = temp_gear[gear_num - 1]
        
        if rotation_direction == -1:
            counterclockwise(gear_num)
            gear[gear_num] = temp_gear[gear_num]
        else:
            clockwise(gear_num)
            gear[gear_num] = temp_gear[gear_num]

        
pprint(gear)     
        
    

