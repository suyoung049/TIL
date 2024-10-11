w, h = 5, 3

def solution(w,h):
    answer = 1
    num_gcd = gcd(w, h)
    gcd_w = w//num_gcd
    gcd_h = h//num_gcd

    if gcd_w < gcd_h:
       remain = gcd_h + (gcd_w -1)
    else:
       remain = gcd_w + (gcd_h - 1)

    answer = (w * h) - (remain * num_gcd)
    return answer

def gcd(a, b):
  for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
      return i
    

solution(w, h)