numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right' 

answer = ''
# 가까운 거리 구하기 위한 좌표 딕셔너리 표시
key_dict = {
    1:(0,0), 2:(0,1), 3:(0,2),
    4:(1,0), 5:(1,1), 6:(1,2),
    7:(2,0), 8:(2,1), 9:(2,2),
    '*':(3,0), 0:(3,1), '#':(3,2), 
}

left = [1, 4, 7]
right = [3, 6, 9]
lhand = '*'
rhand = '#'

for i in numbers:
    if i in left:
        answer += 'L'  # 눌러야 할 키가 왼쪽에서 있을 때
        lhand = i
    elif i in right:
        answer += 'R' # 눌러야 할 키가 오른쪽에 있을 때
        rhand = i
    
    else:
        now = key_dict[i]
        lpos = key_dict[lhand]
        rpos = key_dict[rhand]
        llength = abs((now[0]-lpos[0])) + abs((now[1])-lpos[1])
        rlength = abs((now[0])-rpos[0]) + abs((now[1]-rpos[1])) 
        # 가운데 있는 키는 지금 손의 위치에 따라 가까운 곳에 거리를 구한뒤 지정 거리는 (y,x) 좌표의 차의 절대값


        if llength < rlength:  # 왼쪽 손이 더 가까우면 왼쪽 엄지
            answer += 'L'
            lhand = i
        elif llength > rlength:  # 오른쪽 손이 더 가까우면 오른쪽 엄지
            answer += 'R'
            rhand = i

        else:                    # 거리가 같을 경우 지정해준 손잡이로 지정 
            if hand == 'left':
                answer += 'L'
                lhand = i
            else:
                answer += 'R'
                rhand = i
