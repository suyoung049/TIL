from collections import Counter
lottos, win_nums = [44, 1, 0, 0, 31, 25], 	[31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
  win_count = 0
  min_win = 0
  max_win = 0
  for num in lottos:
    if win_nums.__contains__(num):
      win_count += 1
    
  if win_count == 0:
    min_win = 6
  
  else:
    min_win = 7 - win_count

  zero_count = Counter(lottos)[0]

  if (win_count + zero_count == 0):
    max_win = 6

  else:
    max_win = 7 - (win_count + zero_count)
  return [max_win, min_win]

solution(lottos, win_nums)