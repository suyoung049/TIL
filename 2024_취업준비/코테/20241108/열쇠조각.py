from copy import deepcopy

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def pprint(matrix):
    for x in matrix:
        print(x)

def rotation_90(matrix):
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            rotated_matrix[x][n - 1 - y] = matrix[y][x]
    return rotated_matrix

def check_key(key, new_matrix, start_x, start_y, lock_length):
    # new_matrix를 deepcopy로 복사하여 변경을 시도함
    temp_matrix = deepcopy(new_matrix)
    key_length = len(key)

    # key의 값을 temp_matrix에 추가
    for y in range(key_length):
        for x in range(key_length):
            temp_matrix[start_y + y][start_x + x] += key[y][x]

    # lock의 모든 홈이 맞는지 검사
    for y in range(lock_length):
        for x in range(lock_length):
            if temp_matrix[y + key_length - 1][x + key_length - 1] != 1:
                return False
    return True

def solution(key, lock):
    key_length = len(key)
    lock_length = len(lock)
    extra = key_length - 1
    new_length = lock_length + (extra * 2)
    
    # 확장된 new_matrix 생성 및 중앙에 lock 배치
    new_matrix = [[0 for _ in range(new_length)] for _ in range(new_length)]
    for y in range(lock_length):
        for x in range(lock_length):
            new_matrix[y + extra][x + extra] = lock[y][x]
    
    # rotation_dict를 사용해 각 회전된 key 저장
    rotation_dict = {0: key}
    copy_key = deepcopy(key)
    for i in range(1, 4):
        rotation_key = rotation_90(copy_key)
        rotation_dict[i] = rotation_key
        copy_key = deepcopy(rotation_key)
    
    # 4가지 회전 방향에 대해 key를 테스트
    for rotation in range(4):
        rotated_key = rotation_dict[rotation]
        for y in range(new_length - key_length + 1):
            for x in range(new_length - key_length + 1):
                if check_key(rotated_key, new_matrix, x, y, lock_length):
                    return True
    
    return False

print(solution(key, lock))











solution(key, lock)