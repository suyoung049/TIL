data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501 
sort_by = "date"

def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    data_list = classification_data(data, ext, val_ext)
    sort_list = sort_data(data_list, sort_by)
    
    return answer


def classification_data(data, ext, val_ext):
    data_list = []
    if ext == "code":
        for single in data:
            if single[0] <= val_ext:
                data_list.append(single)
    elif ext == "maximum":
        for single in data:
            if single[2] <= val_ext:
                data_list.append(single)
    elif ext == "remain":
        for single in data:
            if single[3] <= val_ext:
                data_list.append(single)
    else:
        for single in data:
            if single[1] <= val_ext:
                data_list.append(single)
    
    return data_list

def sort_data(data_list, sort_by):
    length = len(data_list) -1
    if sort_by == "remain":
        for i in range(length):
            for j in range(length-i):
                if (data_list[j][3] > data_list[j+1][3]):
                    data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
    elif sort_by == 'code':
        for i in range(length):
          for j in range(length-i):
              if (data_list[j][0] > data_list[j+1][0]):
                  data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
    elif sort_by == "maximum":
        for i in range(length):
          for j in range(length-i):
              if (data_list[j][2] > data_list[j+1][2]):
                  data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
    else:
        for i in range(length):
          for j in range(length-i):
               if (data_list[j][1] > data_list[j+1][1]):
                  data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
    return data_list
                        




solution(data, ext, val_ext, sort_by)