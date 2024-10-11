n = 1
t = 1
m = 5
timetable = 	["08:00", "08:01", "08:02", "08:03"]

# 시간에 관련된 문제는 왠만해서는 int로 변환하려고 노력하기

# 문제의 지문을 리스트나 딕셔너리 데이터 형식으로 변환하려고 노력하기 ex) 셔틀을 태우는건  이중 리스트로 담는 식으로 

def solution(n, t, m, timetable):
    int_time = []
    shuttle_li = [[] for _ in range(n)]
    arrive_li = [ 540 + t * i for i in range(n)]
    # 시간을 int 형으로 변경
    for time in timetable:
        spl_time = time.split(':')
        convert_time = int(spl_time[0]) * 60 + int(spl_time[1])
        int_time.append(convert_time)

    int_time.sort()
    idx = 0
    for i in range(n):
        while len(shuttle_li[i]) < m and idx < len(timetable) and arrive_li[i] >= int_time[idx]:
            shuttle_li[i].append(idx)
            idx += 1

    if len(shuttle_li[-1]) < m:
        return convert_str(arrive_li[-1])
    
    return convert_str(int_time[shuttle_li[-1][-1]] - 1)
    
def convert_str(time):
    hh = time // 60
    mm = time % 60

    str_hh = str(hh)
    str_mm = str(mm)

    if len(str_hh) == 1:
        str_hh = "0" + str_hh

    if len(str_mm) == 1:
        str_mm = "0" + str_mm

    return str_hh + ":" + str_mm

solution(n, t, m, timetable)