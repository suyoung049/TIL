keyinput, board = ["left", "right", "up", "right", "right"], 	[11, 11]

key_dict = {
    "left":(-1, 0),
    "right":(1, 0),
    "up":(0, 1),
    "down":(0, -1)
}
def solution(keyinput, board):
    global key_dict
    answer = [0, 0]
    max_length_x = board[0]//2
    max_length_y = board[1]//2
    for key in keyinput:
        if (-max_length_x <= answer[0] + key_dict[key][0] <= max_length_x and -max_length_y <= answer[1] + key_dict[key][1] <= max_length_y):
            answer[0] = answer[0] + key_dict[key][0]
            answer[1] = answer[1] + key_dict[key][1]
    return answer

solution(keyinput, board)