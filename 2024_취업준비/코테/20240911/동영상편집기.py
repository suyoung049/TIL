video_len = "59:59"
pos = "00:08"
op_start = "00:00"
op_end = "00:05"
commands = ["prev"]

def solution(video_len, pos, op_start, op_end, commands):
    pos_int = int(pos.split(':')[0]) * 60 + int(pos.split(':')[1])
    video_int = int(video_len.split(':')[0]) * 60 + int(video_len.split(':')[1])
    op_start_int = int(op_start.split(':')[0]) * 60 + int(op_start.split(':')[1])
    op_end_int = int(op_end.split(':')[0]) * 60 + int(op_end.split(':')[1])
    
    if op_start_int <= pos_int <= op_end_int:
        pos_int = op_end_int

    for cmd in commands:
        if cmd == "next":
            pos_int += 10
            if video_int - pos_int < 10: 
                pos_int = video_int
        elif cmd == "prev":
            pos_int -= 10
            if pos_int < 10:
                pos_int = 0
        
        if op_start_int <= pos_int <= op_end_int:
            pos_int = op_end_int

    answer = change_string(pos_int)

    return answer

def change_string(pos_int):
    mm = pos_int//60
    ss = pos_int % 60

    if mm < 10:
        str_mm = "0" + str(mm)
    else:
        str_mm = str(mm)
    
    if ss < 10:
        str_ss = "0" + str(ss)
    else:
        str_ss = str(ss)

    
    return str_mm + ":" + str_ss


print(solution(video_len, pos, op_start, op_end, commands))