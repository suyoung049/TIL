import sys

sys.stdin = open("25192_input.txt", "r")

N = int(input())

log_list = []
gom = 0
for i in range(N):
    log_list.append(input())
print(log_list)

list_ = list()
set_ = set(list_)

for log in log_list:
    if log == 'ENTER':
        set_.clear()
    else:
        if log not in set_:
            set_.add(log)
            gom += 1
print(gom)
       
          
